# Import needed libraries
import time
import RPi.GPIO as GPIO
import os

def main():
    #IP addresses of destinations used to test if the internet is up
    destination1 = "8.8.8.8"
    destination2 = "1.1.1.1"
    # Infinate Loop
    while True:
        #Ping both destinations three times
        response1 = os.system("ping -c 3 " + destination1)
        response2 = os.system("ping -c 3 " + destination2)
        #Check response codes from pinging both destinations
        if response1 == 0 or response2 == 0:
            print("UP")
        #If ping tests of both destinations fail, test again after 20 seconds
        else:
            print("DOWN, test again")
            time.sleep(20)
            response1 = os.system("ping -c 3 " + destination1)
            response2 = os.system("ping -c 3 " + destination2)
            if response1 == 0 or response2 == 0:
                print("Recover")
            # If ping tests fail again signal relay switch in order to power down 120V circuit
            else:
                print("Power OFF Modem")
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(23, GPIO.OUT)
                # Open 120V circuit
                GPIO.output(23, GPIO.HIGH)
                print("wait 30 seconds")
                time.sleep(30)
                print("Power back on")
                # After 30 seconds return 120V circuit to closed
                GPIO.output(23, GPIO.LOW)
                GPIO.cleanup()
                # Wait 5 minutes to resume tests to alot time for modem reboot
                print("Wait 5 Minutes to resume testing")
                time.sleep(300)
        # Wait 30 seconds between ping tests        
        time.sleep(30)

if __name__=="__main__":
    main()
