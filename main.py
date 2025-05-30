import can_receiver

def main():
	try:
		bus = can_receiver.get_data_bus()
		while True:
			message = can_receiver.get_can_line(bus)
			if message == None:
				break
	except Exception as e:
		print ("MAIN::unknown exception:", e)

if __name__ == "__main__":
	main()
