

1. Getting Django Set Up Using a Functional Test

Try out functional_test.py

Setup Django


2. Extending Our Functional Test Using the unittest Module

> Terminology: Functional Test == Acceptance Test == End-to-End Test

Write story for your functional test.
They should be human readable.

Let's run and see a failure.

The Python Standard Library’s unittest Module

Let's format our code to use the unittest.TestCase class.

Explain the module a bit. Like setup and tearDown

We rerun and see a more useful information.

### Useful TDD Concepts

User Story
A description of how the application will work from the point of view of the user. Used to structure a functional test.

Expected failure
When a test fails in the way that we expected it to.

Commit!

3. Home page, first Unit Test and our first Django app.

Let's create an app called engagement.

It's not time we differentiate Functional Test and Unit Test.

Steps in doing TDD:
* Write functional test with user stories
* Run and let it fail.
* Think how to make it pass
* Write one or more unittest to define the behavior
* Write application code
* Make the unit test pass.
* Rerun functional test.
* Repeat.

Let's try it!

Sanity check:
Use tests.py from engagement and create a failing test.

Then let's use django test runner to run the test.

./manage.py test

Maybe Let's now talk about Django's Structure. MVC if the audience is not familiar.

Explain we will now need to use django internal helper for testing.

What do we want to test now?

* Can we resolve the URL for the root of the site (“/”) to a particular view function we’ve made?
* Can we make this view function return some HTML which will get the functional test to pass?

Let's now edit our tests.py file to reflect what we want to test.

So our test is telling us we cannot resolve the url.

Here we now add a route using urls.py

We should now be getting an error telling us that the view should be callable.

Alright, let's make the view callable.

Run the test! 
Yohoo! Our first unit test that is passing.


## Unit testing a view
Write the code for testing the index view

Run the test.

Then go through each code cyle with minimal changes at a time.

When the code pass, let's rerun functional test.


4. What Are We Doing with All These Tests? (And, Refactoring)

Let's now write selenium test for the stories.
Rerun the test and you get an error like this:

```
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: header
```

What does that tell us? Explain.


The “Don’t Test Constants” Rule, and Templates to the Rescue

It's now refactoring time.
Move html to templates dir.

Run unit test, it should be failing(TemplateDoesNotExist).

Explain the traceback.

Add app to settings INSTALLED_APPS.

Rerun the test and fix the remaining issues.

Now let's try the Django test client.
We will now use assertion built into django itself.
assertTemplateUsed

Let's try to deliberately fail it.

We can now refactor the name to 'test_uses_index_template'
Remove the test_root_url_resolves test as well because django 
test client is already implicity tesing.

Don't get tempted in tweaking a lot of things at the same time.
When refactoring, work on either the code or the tests, but not both at once.
Show refactoring cat.
http://bit.ly/1iXyRt4

Run Functional Test(Failing)
Let's code some html, currently it's looking for header.


Now we are coding for the next page with url "/send_sms/"

Now we are done with coding the send_sms page with form.

Let's go to the view function for send_sms, it's time for unit test.

Added the test and mocking for send_sms view
