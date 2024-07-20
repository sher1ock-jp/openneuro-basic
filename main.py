import json
from openneuro_query import query_rawdata

import mne

def main(dataset_id, tag):
    print("Fetching sub-001 files...")
    eeg_file = query_rawdata(dataset_id, tag)
    print(json.dumps(eeg_file, indent=2))



if __name__ == "__main__":
    dataset_id = "ds005194"
    tag = "1.1.0"
    
    # main(dataset_id, tag)
    
    # data_path = mne.datasets.sample.data_path()
    # print(f"Sample dataset path: {data_path}")

    # サンプルデータのパスを取得
    sample_data_folder = mne.datasets.sample.data_path()
    
    sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif"
    )

    # 生データを読み込む
    raw = mne.io.read_raw_fif(sample_data_raw_file)

    # データをメモリにロード
    raw.load_data()

    # データの先頭の部分を表示（例: 先頭の5チャンネル、先頭の10サンプル）
    data = raw.get_data()
    print(data[:5, :10])

    # EEGデータを取得して表示
    eeg_data = raw.get_data(picks='eeg')
    print(eeg_data[:, :10])

    # 生データをプロット
    raw.plot(duration=5, n_channels=30)