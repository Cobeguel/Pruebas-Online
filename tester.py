

class Tester
	def add_args():
		parser = argparse.ArgumentParser(description=__doc__)
		parser.add_argument('-i', '--input-device', type=int_or_str,
				                help='input device ID or substring')
		parser.add_argument('-o', '--output-device', type=int_or_str,
				                help='output device ID or substring')
		parser.add_argument('-c', '--channels', type=int, default=2,
				                help='number of channels')
		parser.add_argument('-t', '--dtype', help='audio data type')
		parser.add_argument('-s', '--samplerate', type=float, help='sampling rate')
		parser.add_argument('-b', '--blocksize', type=int, help='block size')
		#parser.add_argument('-l', '--latency', type=float, help='latency in seconds')
		return parser.parse_args()

