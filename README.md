# Lumus


Hello, I came to present an Air gapp technique that I have been developing to extract data via the CaPsLock keyboard LED, the technique consists of taking a something file and converting the text into binary and then the malware in this case can use the CaPsLock LED to send the file to the attacker without him needing the Internet 1 blink of the led means 1, 2 blinks of the led means 0
In the video I am demonstrating the malware writing the word Lumus using the keyboard led
An article in 2019 was released but they used 3 different keys
I managed to do the technique using only capslock
However, extracting long data is time consuming.
For an attacker to get the data he needs to be a little close to the target and records the blinking led
With that he can write the binary in a text file for example seeing the recording of the led
And use some site that converts binary to text
Representing the space was the most difficult task so I decided that the malware should wait 3 seconds before continuing a sequence for me to know it was a space
The purpose of me showing this is to show how malicious attackers can extract data even if the computers are not connected to the internet, even though this type of extraction is time consuming it is something that can be used.
