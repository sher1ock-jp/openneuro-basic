import matplotlib.pyplot as plt
import mne

def load_data():
    
    sample_data_folder = mne.datasets.sample.data_path()
    
    sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif"
    )

    raw = mne.io.read_raw_fif(sample_data_raw_file)

    print(raw)

    raw.load_data()

    data = raw.get_data()
    print(data[:5, :10])

    eeg_data = raw.get_data(picks='eeg')
    print(eeg_data[:, :10])

    # meg_data_mag = raw.get_data(picks='mag')
    # print(meg_data_mag[:, :10])

    # パワースペクトル密度（PSD）を計算してプロット
    psd_fig = raw.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)
    
    # PSDプロットをファイルに保存
    psd_fig.savefig('psd_plot.png')

    # 生データのトレースをプロット
    raw_fig = raw.plot(duration=5, n_channels=30, show=False)
    
    # 生データのトレースプロットをファイルに保存
    raw_fig.savefig('raw_plot.png')

    plt.show()

    plt.show()