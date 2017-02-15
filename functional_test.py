from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# JayR went to the website, he notice the title as "Surveyor".
assert 'Surveyor' in browser.title

# He saw a button that invites him to send an SMS and clicked the button

# On the next page, there's header that says:
# Fill this information to send an SMS

# He notice that there are 2 fields and a button.
# The first field is for adding contact information.
# The second field is for adding the message.
# Lastly a button to submit the form.

# So he add his contact number on the first field. 09152087801
# And added message on the second.
# What is your Full Name?

# Lastly he clicked the submit button!

# After clicking the button he is immediately redirected to the home page.
# With a notification that says, "Message sent, please wait for reply!"

# He still didn't see any reply.

# He got a notification from his phone, check and recieve the message
# that he sent earlier. He immediately replied:
# Elpedio Adoptante

# He tries to refresh the page and saw the message like this.
# Number        Name
# 09152087801   JayR

# He is now happy and closes the browser.
browser.quit()

