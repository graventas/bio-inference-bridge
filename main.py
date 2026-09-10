import numpy as np
import time

class SpikeEncoder:
    """
    Mengonversi input posisi/koordinat menjadi frekuensi impuls listrik (Spike Rate).
    """
    def __init__(self, num_channels=8):
        self.num_channels = num_channels

    def encode_position(self, position_val, max_val=100):
        """
        Sederhana: Semakin dekat objek, semakin tinggi frekuensi impuls pada channel terkait.
        """
        normalized = np.clip(position_val / max_val, 0, 1)
        # Menghasilkan probabilitas firing spike
        spike_probabilities = np.random.rand(self.num_channels) < normalized
        return spike_probabilities.astype(int)

class DummyBioDecoder:
    """
    Menerjemahkan respons impuls sel/SNN menjadi aksi permainan.
    """
    def decode_action(self, spike_response):
        left_channel_spikes = np.sum(spike_response[:4])
        right_channel_spikes = np.sum(spike_response[4:])
        
        if left_channel_spikes > right_channel_spikes:
            return "MOVE_LEFT"
        elif right_channel_spikes > left_channel_spikes:
            return "MOVE_RIGHT"
        return "HOLD"

def main():
    print("=== Bio-Inference Bridge (PoC Simulation) ===")
    encoder = SpikeEncoder(num_channels=8)
    decoder = DummyBioDecoder()

    # Simulasi 5 frame pergerakan game
    fake_ball_positions = [10, 35, 70, 90, 40]

    for frame, pos in enumerate(fake_ball_positions):
        spikes = encoder.encode_position(pos)
        action = decoder.decode_action(spikes)
        print(f"Frame {frame+1} | Posisi Bola: {pos:2d} | Sinyal Impuls: {spikes} | Aksi Output: {action}")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
