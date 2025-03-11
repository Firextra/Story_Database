from django.test import TestCase
from .models import UniverseDatabase, CharacterDatabase, ChaptersDatabase, TalesDatabase, User
from django.urls import reverse
import time


class CharacterDatabaseCase(TestCase):
    def setUp(self): #create records in databases
        universe1 = UniverseDatabase.objects.create(Name="Universe1", UniverseAuthor="seneca", UniverseDescription="1", UniverseNumber=1)
        universe406 = UniverseDatabase.objects.create(Name="Universe406", UniverseAuthor="seneca", UniverseDescription="406", UniverseNumber=406)
        CharacterDatabase.objects.create(Name="Store Assistant", Author="seneca", CharacterDescription="He works at a supermarket", UniverseNumber=universe1)
        CharacterDatabase.objects.create(Name="X", Author="seneca", CharacterDescription="Assassin Droid", UniverseNumber=universe406)

    def test_character_fetch(self):
        universe1 = UniverseDatabase.objects.get(Name="Universe1") #fetch records from database
        universe406 = UniverseDatabase.objects.get(Name="Universe406")
        StoreAssistant = CharacterDatabase.objects.get(Name="Store Assistant")
        DroidX = CharacterDatabase.objects.get(Name="X")
        
        self.assertEqual(StoreAssistant.Author, "seneca") #test if author is correct
        self.assertEqual(StoreAssistant.CharacterDescription, "He works at a supermarket") #test if the description is correct
        self.assertEqual(StoreAssistant.UniverseNumber, universe1) #test if the universe number is correct

        self.assertEqual(DroidX.Author, "seneca") #test if author is correct
        self.assertEqual(DroidX.CharacterDescription, "Assassin Droid") #test if the description is correct
        self.assertEqual(DroidX.UniverseNumber, universe406) #test if the universe number is correct
        


class TestProfilePage(TestCase):

    def test_user_access_for_unauthorised(self):    #tests to ensure that unathorised access to profile page is redirected correctly
        response = self.client.get(reverse('ProfilePage')) #attempting to access the profile page
        self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('ProfilePage')}") #tests to ensure that the user has returned back to the login instead of profile page
        

    def test_user_access_for_authorised(self): #tests to ensure a logged in individual can access their profile
        User.objects.create_user(username="testtest", password="fire1234", email="pork.bacon@gmail.com") #create user

        login_successful = self.client.login(username="testtest", password="fire1234") #login user
        response = self.client.get(reverse('ProfilePage')) #tests whether user can access their profile

        self.assertTrue(login_successful, "Test Failed") #prints test failed if the user is not logged in successful
        self.assertContains(response, 'testtest')

class NavigationTest(TestCase):

    def test_loginpage(self):
        response = self.client.get(reverse('login')) 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/CharacterArticles/"') #test navbar items
        self.assertContains(response, 'href="/UniverseArticles/"')
        self.assertContains(response, 'href="/TalesAndChapters/"')
        self.assertContains(response, 'href="/login/"')
        self.assertContains(response, 'href="/"')  #homepage


class RegisterForm(TestCase):
    def test_Register_form_valid(self):

        form_data = {   #create valid form
            'username': 'SteveVerse',
            'email': 'Steve.Verse@gmail.com',
            'password1': "software123",
            'password2': "software123"
        }

        response = self.client.post(reverse('register'), data=form_data, follow=True)       #goto register page with the form

        self.assertEqual(response.status_code, 200)                     #test if successful
        self.assertTrue(User.objects.filter(username='SteveVerse').exists())    #test if user existsnow
        self.assertContains(response, "Login")  #redirect

    def test_create_Character_form_invalid(self):
        
        form_data = { #incorrect form
            'username': '',
            'email': 'Stevegmail',
            'password1': "software123",
            'password2': "software124"
        }
        response = self.client.post(reverse('register'), data=form_data, follow=True) #goto register page with the form

        self.assertEqual(response.status_code, 200)     #test form

        self.assertTrue("form" in response.context)     #check if the form is returned after invalid form submitted
        form = response.context['form'] #get the form

        self.assertFormError(form, 'username', 'This field is required.') #specific error messages for each field
        self.assertFormError(form, 'email', 'Enter a valid email address.')
        self.assertFormError(form, 'password2', 'The two password fields didn’t match.')


        self.assertFalse(User.objects.exists()) #checks to see if teh object does not exist


class PageResponseTimeTest(TestCase):
    def test_page_response_time(self):
        urls = [reverse('login'), reverse('UniverseArticles'), reverse('CreateUniverse'),]  #testing pages

        MaxResponse = 0.6 #max response time we want

        for url in urls: #go through each url
            StartTime = time.time() #start clock
            response = self.client.get(url) #get the url
            EndTime = time.time() #end clock

            duration = EndTime - StartTime #get time
            print(f"Response time for {url}: {duration} seconds") #display result for each url

            self.assertLess(duration, MaxResponse, f"Response Time for {url} exceeded goal response time") #if time exceeded max response time, return error

class SQLResponseTime(TestCase):
    def setUp(self): #create records in databases
        universe1 = UniverseDatabase.objects.create(Name="Universe1", UniverseAuthor="seneca", UniverseDescription="1", UniverseNumber=1)
        universe406 = UniverseDatabase.objects.create(Name="Universe406", UniverseAuthor="seneca", UniverseDescription="406", UniverseNumber=406)
        CharacterDatabase.objects.create(Name="Store Assistant", Author="seneca", CharacterDescription="He works at a supermarket", UniverseNumber=universe1)
        CharacterDatabase.objects.create(Name="X", Author="seneca", CharacterDescription="Assassin Droid", UniverseNumber=universe406)

    def test_character_fetch(self):
        universe1 = UniverseDatabase.objects.get(Name="Universe1") #fetch records from database
        universe406 = UniverseDatabase.objects.get(Name="Universe406")

        StartTime = time.time() #start clock
        StoreAssistant = CharacterDatabase.objects.get(Name="Store Assistant")
        DroidX = CharacterDatabase.objects.get(Name="X")
        EndTime = time.time() #end clock

        duration = EndTime - StartTime #get time
        print(f"Response time for the query: {duration} seconds") #display result for the time