import datetime

from Service.clientCardService import ClientCardService
from Service.movieGenerator import MovieGenerator
from Service.movieService import MovieService
from Service.reservationService import ReservationService
from Service.undoRedoService import UndoRedoService


class Console:

    def __init__(self, movieService: MovieService, cardService: ClientCardService,
                 reservationService: ReservationService, movieGenerator: MovieGenerator,
                 undoRedoService: UndoRedoService):
        self.movieService = movieService
        self.cardService = cardService
        self.reservationService = reservationService
        self.movieGenerator = movieGenerator
        self.undoRedoService = undoRedoService

    def runMenu(self):
        while True:
            print("1. CRUD movie")
            print("2. CRUD client card")
            print("3. CRUD reservation")
            print("4. Functionalities")
            print("u. Undo")
            print("r. Redo")
            print("x. Exit")
            option = input("Enter an option: ")
            if option == "1":
                self.uiRunCrudMovieMenu()
            elif option == "2":
                self.uiRunCrudCardMenu()
            elif option == "3":
                self.uiRunCrudReservationMenu()
            elif option == "4":
                self.uiFunctionalitiesMenu()
            elif option.lower() == "u":
                self.undoRedoService.undo()
            elif option.lower() == "r":
                self.undoRedoService.redo()
            elif option.lower() == "x":
                break
            else:
                print("Wrong option, please retry!")

    def uiRunCrudMovieMenu(self):
        while True:
            print("1. Add movie")
            print("2. Delete movie")
            print("3. Update movie")
            print("a. Show all movies")
            print("x. Exit")
            option = input("Enter an option: ")
            if option == "1":
                self.uiAddMovie()
            elif option == "2":
                self.uiDeleteMovie()
            elif option == "3":
                self.uiUpdateMovie()
            elif option.lower() == "a":
                self.uiShowallMovies()
            elif option.lower() == "x":
                break
            else:
                print("Wrong option, please retry!")

    def uiAddMovie(self):
        try:
            idEntity = input("Enter the movie id: ")
            title = input("Enter the movie title: ")
            releaseYear = int(input("Enter the movie's release year: "))
            ticketPrice = float(input("Enter the movie's ticket price: "))
            inProgram = input("Enter if the movie is in program or not (yes/no): ")
            self.movieService.addMovie(idEntity, title, releaseYear, ticketPrice, inProgram)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiDeleteMovie(self):
        try:
            idEntity = input("Enter the movie's id you want to delete: ")
            self.movieService.deleteMovie(idEntity)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiUpdateMovie(self):
        try:
            idEntity = input("Enter the new movie id: ")
            title = input("Enter the new movie title: ")
            releaseYear = int(input("Enter the new movie's release year: "))
            ticketPrice = float(input("Enter the new movie's ticket price: "))
            inProgram = input("Enter if the movie is in program or not (yes/no): ")
            self.movieService.updateMovie(idEntity, title, releaseYear, ticketPrice, inProgram)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiShowallMovies(self):
        for movie in self.movieService.getAll():
            print(movie)

    def uiRunCrudCardMenu(self):
        while True:
            print("1. Add client card")
            print("2. Delete client card")
            print("3. Update client card")
            print("a. Show all cards")
            print("x. Exit")
            option = input("Enter an option: ")
            if option == "1":
                self.uiAddCard()
            elif option == "2":
                self.uiDeleteCard()
            elif option == "3":
                self.uiUpdateCard()
            elif option.lower() == "a":
                self.uiShowallCards()
            elif option.lower() == "x":
                break
            else:
                print("Wrong option, please retry!")

    def uiAddCard(self):
        try:
            idEntity = input("Enter the card id: ")
            name = input("Enter the client's  name: ")
            surname = input("Enter the client's surname: ")
            CNP = input("Enter the CNP: ")
            birthDate = datetime.datetime.strptime(input("Enter the client's birth date(DD.MM.YYYY): "), "%d.%m.%Y")
            birthDateString = datetime.datetime.strftime(birthDate, "%d.%m.%Y")
            registrationDate = datetime.datetime.strptime(input("Enter the card registration date(DD.MM.YYYY): "),
                                                          "%d.%m.%Y")
            registrationDateString = datetime.datetime.strftime(registrationDate, "%d.%m.%Y")
            points = int(input("Enter the number of points on the card: "))
            self.cardService.addCard(idEntity, name, surname, CNP, birthDateString, registrationDateString, points)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiDeleteCard(self):
        try:
            idEntity = input("Enter the card id that you want to delete: ")
            self.cardService.deleteCard(idEntity)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiUpdateCard(self):
        try:
            idEntity = input("Enter the card id: ")
            name = input("Enter the new client's  name: ")
            surname = input("Enter the new client's surname: ")
            CNP = input("Enter the new CNP: ")
            birthDate = datetime.datetime.strptime(input("Enter the client's birth date(DD.MM.YYYY): "), "%d.%m.%Y")
            birthDateString = datetime.datetime.strftime(birthDate, "%d.%m.%Y")
            registrationDate = datetime.datetime.strptime(input("Enter the card registration date(DD.MM.YYYY): "),
                                                          "%d.%m.%Y")
            registrationDateString = datetime.datetime.strftime(registrationDate, "%d.%m.%Y")
            points = int(input("Enter the number of points on the card: "))
            self.cardService.updateCard(idEntity, name, surname, CNP, birthDateString, registrationDateString, points)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiShowallCards(self):
        for card in self.cardService.getAll():
            print(card)

    def uiRunCrudReservationMenu(self):
        while True:
            print("1. Add reservation")
            print("2. Delete reservation")
            print("3. Update reservation")
            print("a. Show all reservations")
            print("x. Exit")
            option = input("Enter an option: ")
            if option == "1":
                self.uiAddReservation()
            elif option == "2":
                self.uiDeleteReservation()
            elif option == "3":
                self.uiUpdateReservation()
            elif option.lower() == "a":
                self.uiShowallReservations()
            elif option.lower() == "x":
                break
            else:
                print("Wrong option, please retry!")

    def uiAddReservation(self):
        try:
            idEntity = input("Enter the reservation id: ")
            idMovie = input("Enter the movie id: ")
            idCard = input("Enter the card id: ")
            date = datetime.datetime.strptime(input("Enter the reservation date(DD.MM.YYYY): "), "%d.%m.%Y")
            dateString = datetime.datetime.strftime(date, "%d.%m.%Y")
            hour = datetime.datetime.strptime(input("Enter the reservation hour(HH:MM): "), "%H:%M")
            hourString = datetime.datetime.strftime(hour, "%H:%M")
            self.reservationService.addReservation(idEntity, idMovie, idCard, dateString, hourString)
            if idCard == "0":
                print(f"No points added on the card.")
            else:
                print(f"On the card {idCard} were added {self.reservationService.acumulatePoints(idMovie)}"
                      f" points. The total is {self.cardService.getById(idCard).points}.")
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiDeleteReservation(self):
        try:
            idEntity = input("Enter the reservation's id that you want to delete: ")
            self.reservationService.deleteReservation(idEntity)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiUpdateReservation(self):
        try:
            idEntity = input("Enter the reservation id: ")
            idMovie = input("Enter the movie id: ")
            idCard = input("Enter the card id: ")
            date = datetime.datetime.strptime(input("Enter the reservation date(DD.MM.YYYY): "), "%d.%m.%Y")
            dateString = datetime.datetime.strftime(date, "%d.%m.%Y")
            hour = datetime.datetime.strptime(input("Enter the reservation hour(HH:MM): "), "%H:%M")
            hourString = datetime.datetime.strftime(hour, "%H:%M")
            self.reservationService.updateReservation(idEntity, idMovie, idCard, dateString, hourString)
            if idCard == "0":
                print(f"No points added on the card.")
            else:
                points = self.cardService.getById(idEntity).points
                print(f"On the card {idCard} were added {self.reservationService.acumulatePoints(idMovie)}"
                      f" points. The total is {points}.")
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiShowallReservations(self):
        for reservation in self.reservationService.getAll():
            print(reservation)

    def uiOrderedCardsByPointsReverse(self):
        if not self.cardService.orderedCardsByPointsReverse():
            print("No cards to show.")
        else:
            for card in self.cardService.orderedCardsByPointsReverse():
                print(card)

    def uiGenerateRandomMovies(self):
        try:
            n = int(input("Give the number of movies you want to generate: "))
            self.movieGenerator.generateRandomMovies(n)
            for movie in self.movieGenerator.getAll():
                print(movie)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiFunctionalitiesMenu(self):
        while True:
            print("1. Search movies and card. Search full text.")
            print("2. Show all reservations between two hours.")
            print("3. Show movies ordered in reverse by the number of reservations.")
            print("4. Show the cards ordered in reverse by the number of points.")
            print("5. Delete reservations between two dates")
            print("6. Add points to the cards that have the birthdate between two dates.")
            print("s. Delete in cascade (movies).")
            print("r. Generate random movies.")
            print("x. Exit.")
            option = input("Enter an option: ")
            if option == "1":
                while True:
                    print("1. Search movies")
                    print("2. Search clients")
                    print("x. Exit")
                    opt = input("Enter an option: ")
                    if opt == "1":
                        string = input("Enter the string you want to search: ")
                        movies = self.movieService.searchTextMovie(string)
                        if not movies:
                            print("No movies found.")
                        else:
                            for movie in movies:
                                print(movie)
                    elif opt == "2":
                        string = input("Enter the string you want to search: ")
                        cards = self.cardService.searchTextCard(string)
                        if not cards:
                            print("No cards found. ")
                        else:
                            for card in cards:
                                print(card)
                    elif opt.lower() == "x":
                        break
                    else:
                        print("Wrong option, please retry!")
            elif option == "2":
                self.uiReservationsBetweenHours()
            elif option == "3":
                self.uiOrderMoviesByReservationsReverse()
            elif option == "4":
                self.uiOrderedCardsByPointsReverse()
            elif option == "5":
                self.uiDeleteReservationsBetweenDates()
            elif option == "6":
                self.uiAddPoints()
            elif option.lower() == "s":
                self.uiDeleteInCascade()
            elif option.lower() == "r":
                self.uiGenerateRandomMovies()
            elif option.lower() == "x":
                break
            else:
                print("Optiune gresita ! Reincercati ")

    def uiOrderMoviesByReservationsReverse(self):
        if not self.reservationService.orderMoviesByReservationsReverse():
            print("No movies found.")
        else:
            for movie in self.reservationService.orderMoviesByReservationsReverse():
                print(movie)

    def uiReservationsBetweenHours(self):
        try:
            hour1 = datetime.datetime.strptime(input("Enter the first hour: "), "%H:%M")
            hour2 = datetime.datetime.strptime(input("Enter the second hour: "), "%H:%M")
            result = []
            self.reservationService.reservationsBetweenHours(hour1, hour2, self.reservationService.getAll(), result)
            if not result:
                print("No reservations found. ")
            else:
                for reservation in result:
                    print(reservation)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiDeleteReservationsBetweenDates(self):
        try:
            date1 = datetime.datetime.strptime(input("Enter the first date: "), "%d.%m.%Y")
            date2 = datetime.datetime.strptime(input("Enter the second date: "), "%d.%m.%Y")
            self.reservationService.deleteReservationsBetweenDates(date1, date2)
            print("Reservations deleted. ")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiAddPoints(self):
        try:
            date1 = datetime.datetime.strptime(input("Enter the first date: "), "%d.%m.%Y")
            date2 = datetime.datetime.strptime(input("Dati a doua data: "), "%d.%m.%Y")
            value = int(input("Enter the number of points you want to add: "))
            result = self.cardService.addPoints(date1, date2, value)
            if not result:
                print("No cards between the specified dates. ")
            else:
                print(f"Points were added")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiDeleteInCascade(self):
        try:
            idMovie = input("Enter the movie id that you want to delete: ")
            self.reservationService.deleteInCascade(idMovie)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
