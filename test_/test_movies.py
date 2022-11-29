from POM.movies import Bms_Movies
import time

class TestMovies:

    def test_movies(self, _driver):
        movies_obj = Bms_Movies(_driver)

        movies_obj.choose_location()
        movies_obj.click_moviesbutton()
        movies_obj.choose_English()
        movies_obj.choose_movie()
        movies_obj.click_BookTickets()
        movies_obj.choose_3D()
        movies_obj.choose_date()
        time.sleep(3)
        movies_obj.choosing_showtimings()
        movies_obj.chooseAccept_termsandconditions()
        movies_obj.select_no_of_seats()
        movies_obj.click_Selectseats()
        movies_obj.select_desiredseat()
        movies_obj.click_paybutton()

# pytest --html=report.html


