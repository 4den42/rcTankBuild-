import inputs

def main():
    print("Listening for controller input... (CTRL+C to quit)")

    try:
        while True:
            events = inputs.get_gamepad()
            for event in events:
                # Show a readable event printout
                print(f"Event: type={event.ev_type}, code={event.code}, state={event.state}")

                # Example handling of a button press (A button on Xbox)
                if event.ev_type == 'Key' and event.code == 'BTN_SOUTH' and event.state == 1:
                    print("A button pressed!")

                # Example for left stick up/down
                if event.ev_type == 'Absolute' and event.code == 'ABS_Y':
                    print(f"Left stick Y axis moved to {event.state}")

                # Example for right trigger
                if event.ev_type == 'Absolute' and event.code == 'ABS_RZ':
                    print(f"Right trigger value: {event.state}")

    except KeyboardInterrupt:
        print("\nStopped listening. Exiting...")

if __name__ == "__main__":
    main()
