import datetime
import blynk_http as blk

token = '3bf5264b10fb4b84a1f8dd1d9f3107b0'

# initiate Blynk given a token
# you can get your token by creating a project on the Bylnk mobile app.
blk.init(token)

# write to pin
#blk.write('V0', datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))

blk.write('V0', '100')
blk.write('V1', '200')
blk.write('V2', '300')
blk.write('V3', '10')

# read from pin
print((blk.read('V0')))

blk.get_project_property()



# Send an email notification
#blk.set_email_address("automatic.dai@gmail.com")
#blk.send_email("Test email")

# Push a notification to your phone
#blk.send_notification('This is a test message')
