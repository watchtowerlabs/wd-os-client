#!/usr/bin/env python3

import logging
from argparse import ArgumentParser
from datetime import datetime, timedelta

import matplotlib
import matplotlib.dates as mdates  # isort: skip
import numpy as np  # isort: skip
from matplotlib.dates import date2num

matplotlib.use('Agg')

import matplotlib.pyplot as plt  # isort:skip # noqa: E402 # pylint: disable=C0411,C0412,C0413

LOGGER = logging.getLogger(__name__)

OFFSET_IN_STDS = -2.0
SCALE_IN_STDS = 8.0


class EmptyArrayError(Exception):
    """Empty data array exception"""


def _read_waterfall(datafile_path):
    """Read waterfall data file

    :param datafile_path: Path to data file
    :type datafile_path: str
    :raises EmptyArrayError: Empty waterfall data
    :return: Waterfall data
    :rtype: dict
    """
    LOGGER.info('Reading waterfall file')

    datafile = open(datafile_path, mode='rb')

    waterfall = {
        'timestamp': np.fromfile(datafile, dtype='|S32', count=1)[0],
        'nchan': np.fromfile(datafile, dtype='>i4', count=1)[0],
        'samp_rate': np.fromfile(datafile, dtype='>i4', count=1)[0],
        'nfft_per_row': np.fromfile(datafile, dtype='>i4', count=1)[0],
        'center_freq': np.fromfile(datafile, dtype='>f4', count=1)[0],
        'endianess': np.fromfile(datafile, dtype='>i4', count=1)[0]
    }
    data_dtypes = np.dtype([('tabs', 'int64'), ('spec', 'float32', (waterfall['nchan'], ))])
    waterfall['data'] = np.fromfile(datafile, dtype=data_dtypes)
    if not waterfall['data'].size:
        raise EmptyArrayError

    datafile.close()

    return waterfall


def _compress_waterfall(waterfall):
    """Compress spectra of waterfall

    :param waterfall: Watefall data
    :type waterfall: dict
    :return: Compressed spectra
    :rtype: dict
    """
    spec = waterfall['data']['spec']
    std = np.std(spec, axis=0)
    offset = np.mean(spec, axis=0) + OFFSET_IN_STDS * std
    scale = SCALE_IN_STDS * std / 255.0
    values = np.clip((spec - offset) / scale, 0.0, 255.0).astype('uint8')

    return {'offset': offset, 'scale': scale, 'values': values}


def _get_waterfall(datafile_path):
    """Get waterfall data

    :param datafile_path: Path to data file
    :type datafile_path: str_array
    :return: Waterfall data including compressed data
    :rtype: dict
    """
    waterfall = _read_waterfall(datafile_path)

    nint = waterfall['data']['spec'].shape[0]
    waterfall['trel'] = np.arange(nint) * waterfall['nfft_per_row'] * waterfall['nchan'] / float(
        waterfall['samp_rate'])
    waterfall['freq'] = np.linspace(-0.5 * waterfall['samp_rate'],
                                    0.5 * waterfall['samp_rate'],
                                    waterfall['nchan'],
                                    endpoint=False)
    waterfall['compressed'] = _compress_waterfall(waterfall)

    return waterfall


class Waterfall():  # pylint: disable=R0903
    """Parse waterfall data file

    :param datafile_path: Path to data file
    :type datafile_path: str_array
    """

    def __init__(self, datafile_path):
        """Class constructor"""
        self.data = _get_waterfall(datafile_path)

    def plot(self, figure_path, vmin=None, vmax=None):
        """Plot waterfall into a figure

        :param figure_path: Path of figure file to save
        :type figure_path: str
        :param vmin: Minimum value range
        :type vmin: int
        :param vmax: Maximum value range
        :type vmax: int
        """
        tmin = np.min(self.data['data']['tabs'] / 1000000.0)
        tmax = np.max(self.data['data']['tabs'] / 1000000.0)
        fmin = np.min(self.data['freq'] / 1000.0)
        fmax = np.max(self.data['freq'] / 1000.0)
        timefmt = '%Y-%m-%dT%H:%M:%S.%fZ'
        t_ref = datetime.strptime(self.data['timestamp'].decode('utf-8'), timefmt)
        dt_min = t_ref + timedelta(seconds=tmin)
        dt_max = t_ref + timedelta(seconds=tmax)
        if vmin is None or vmax is None:
            vmin = -100
            vmax = -50
            c_idx = self.data['data']['spec'] > -200.0
            if np.sum(c_idx) > 100:
                data_mean = np.mean(self.data['data']['spec'][c_idx])
                data_std = np.std(self.data['data']['spec'][c_idx])
                vmin = data_mean - 2.0 * data_std
                vmax = data_mean + 6.0 * data_std
        plt.figure(figsize=(10, 20))
        plt.imshow(self.data['data']['spec'],
                   origin='lower',
                   aspect='auto',
                   interpolation='None',
                   extent=[fmin, fmax, date2num(dt_min),
                           date2num(dt_max)],
                   vmin=vmin,
                   vmax=vmax,
                   cmap='viridis')
        axis = plt.gca()
        axis.yaxis_date()
        axis.yaxis.set_major_locator(mdates.MinuteLocator(interval=1))
        axis.yaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        axis2 = axis.twinx()
        axis2.set_ylim(tmin, tmax)
        plt.xlabel('Frequency (kHz)')
        axis.set_ylabel('Time (UTC)')
        axis2.set_ylabel('Time (seconds)')
        fig = plt.colorbar(aspect=50, pad=0.1)
        fig.set_label('Power (dB)')
        plt.savefig(figure_path, bbox_inches='tight')
        plt.close()


def main():
    parser = ArgumentParser(description='Make a waterfall plot')
    parser.add_argument('data_path', help='Data path (dat file)')
    parser.add_argument('png_path', help='Output path (png file)')
    args = parser.parse_args()
    waterfall = Waterfall(args.data_path)
    waterfall.plot(args.png_path)


if __name__ == '__main__':
    main()
