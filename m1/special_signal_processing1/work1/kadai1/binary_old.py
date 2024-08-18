import struct

def read_wav_file(file_path):
    with open(file_path, 'rb') as file:
        # RIFFヘッダの読み込み
        riff = file.read(12)
        riff_id, riff_size, wave_id = struct.unpack('<4sI4s', riff)
        
        if riff_id != b'RIFF' or wave_id != b'WAVE':
            raise ValueError("これはWAVファイルではありません")
        
        # fmtチャンクの読み込み
        fmt_header = file.read(8)
        fmt_id, fmt_size = struct.unpack('<4sI', fmt_header)
        
        if fmt_id != b'fmt ':
            raise ValueError("fmtチャンクが見つかりません")
        
        fmt_data = file.read(fmt_size)
        audio_format, num_channels, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack('<HHIIHH', fmt_data)
        
        print(f"Audio Format: {audio_format}")
        print(f"Number of Channels: {num_channels}")
        print(f"Sample Rate: {sample_rate}")
        print(f"Byte Rate: {byte_rate}")
        print(f"Block Align: {block_align}")
        print(f"Bits per Sample: {bits_per_sample}")
        
        # dataチャンクの読み込み
        data_header = file.read(8)
        data_id, data_size = struct.unpack('<4sI', data_header)
        
        if data_id != b'data':
            raise ValueError("dataチャンクが見つかりません")
        
        print(f"Data Size: {data_size} bytes")
        
        # 音声データの読み込み
        audio_data = file.read(data_size)
        
        return audio_data

def main():
    file_path = 'arayurugennzituwo.wav'  # WAVファイルのパスを指定してください
    audio_data = read_wav_file(file_path)
    print("Audio Data:", audio_data[:64])  # 最初の64バイトを表示

if __name__ == "__main__":
    main()
