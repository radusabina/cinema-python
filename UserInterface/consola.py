import datetime

from Service.cardClientService import CardClientService
from Service.filmGenerator import FilmGenerator
from Service.filmService import FilmService
from Service.rezervareService import RezervareService
from Service.undoRedoService import UndoRedoService


class Console:

    def __init__(self, filmService: FilmService,
                 cardService: CardClientService,
                 rezervareService: RezervareService,
                 filmGenerator: FilmGenerator,
                 undoRedoService: UndoRedoService):
        self.filmService = filmService
        self.cardService = cardService
        self.rezervareService = rezervareService
        self.filmGenerator = filmGenerator
        self.undoRedoService = undoRedoService

    def runMenu(self):
        while True:
            print("1. CRUD film")
            print("2. CRUD card client")
            print("3. CRUD rezervare")
            print("4. Functionalitati")
            print("u. Undo")
            print("r. Redo")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiRunCrudFilmMenu()
            elif optiune == "2":
                self.uiRunCrudCardMenu()
            elif optiune == "3":
                self.uiRunCrudRezervareMenu()
            elif optiune == "4":
                self.uiFunctionalitatiMenu()
            elif optiune.lower() == "u":
                self.undoRedoService.undo()
            elif optiune.lower() == "r":
                self.undoRedoService.redo()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati :)")

    def uiRunCrudFilmMenu(self):
        while True:
            print("1. Adauga film")
            print("2. Sterge film")
            print("3. Modifica film")
            print("a. Afiseaza filme")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiAdaugaFilm()
            elif optiune == "2":
                self.uiStergeFilm()
            elif optiune == "3":
                self.uiModificaFilm()
            elif optiune.lower() == "a":
                self.uiShowallFilme()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def uiAdaugaFilm(self):
        try:
            idEntitate = input("Dati id-ul filmului: ")
            titlu = input("Dati titlul filmului: ")
            anAparitie = int(input("Dati anul aparitiei filmului: "))
            pretBilet = float(input("Dati pretul biletului: "))
            inProgram = input("Specificati daca filmul"
                              " este in program (da/nu): ")
            self.filmService.adaugaFilm(idEntitate, titlu, anAparitie,
                                        pretBilet, inProgram)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiStergeFilm(self):
        try:
            idEntitate = input("Dati id-ul filmului "
                               "pe care doriti sa-l stergeti: ")
            self.filmService.stergeFilm(idEntitate)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaFilm(self):
        try:
            idEntitate = input("Dati id-ul filmului pe care"
                               " doriti sa-l modificati: ")
            titlu = input("Dati noul titlu al filmului: ")
            anAparitie = int(input("Dati noul an al aparitiei filmului: "))
            pretBilet = float(input("Dati noul pret al biletului: "))
            inProgram = input("Specificati daca noul film "
                              "este in program (da/nu): ")
            self.filmService.modificaFilm(idEntitate, titlu,
                                          anAparitie, pretBilet, inProgram)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiShowallFilme(self):
        for film in self.filmService.getAll():
            print(film)

    def uiRunCrudCardMenu(self):
        while True:
            print("1. Adauga card client")
            print("2. Sterge card client")
            print("3. Modifica card client")
            print("a. Afiseaza carduri")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiAdaugaCard()
            elif optiune == "2":
                self.uiStergeCard()
            elif optiune == "3":
                self.uiModificaCard()
            elif optiune.lower() == "a":
                self.uiShowallCarduri()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita! Reincercati")

    def uiAdaugaCard(self):
        try:
            idEntitate = input("Dati id-ul cardului: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            CNP = input("Dati CNP-ul: ")
            dataNasterii = datetime.datetime.strptime(input(
                "Dati data nasterii clientului(DD.MM.YYYY): "), "%d.%m.%Y")
            dataNasteriiString = datetime.datetime.strftime(
                dataNasterii, "%d.%m.%Y")
            dataInregistrarii = datetime.datetime.strptime(input(
                "Dati data inregistrarii clientului(DD.MM.YYYY): "),
                "%d.%m.%Y")
            dataInregistrariiString = datetime.datetime.strftime(
                dataInregistrarii, "%d.%m.%Y")
            puncteCumulate = int(input("Dati numarul de puncte"
                                       " cumulate pe card: "))
            self.cardService.adaugaCard(idEntitate, nume, prenume, CNP,
                                        dataNasteriiString,
                                        dataInregistrariiString,
                                        puncteCumulate)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiStergeCard(self):
        try:
            idEntitate = input("Dati id-ul cardului client "
                               "pe care doriti sa-l stergeti: ")
            self.cardService.stergeCard(idEntitate)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaCard(self):
        try:
            id_card = input("Dati id-ul cardului pe care doriti"
                            " sa-l modificati: ")
            nume = input("Dati noul nume al clientului: ")
            prenume = input("Dati noul prenume al clientului: ")
            CNP = input("Dati noul CNP: ")
            dataNasterii = datetime.datetime.strptime(input(
                "Dati noua data a nasterii clientului(DD.MM.YYYY): "),
                "%d.%m.%Y")
            dataNasteriiString = datetime.datetime.strftime(
                dataNasterii, "%d.%m.%Y")
            dataInregistrarii = datetime.datetime.strptime(input(
                "Dati noua data a inregistarii cardului(DD.MM.YYYY):"
                " "), "%d.%m.%Y")
            dataInregistrariiString = datetime.datetime.strftime(
                dataInregistrarii, "%d.%m.%Y")
            puncteCumulate = int(input("Dati numarul de puncte"
                                       " cumulate pe card: "))
            self.cardService.modificaCard(id_card, nume, prenume, CNP,
                                          dataNasteriiString,
                                          dataInregistrariiString,
                                          puncteCumulate)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiShowallCarduri(self):
        for card in self.cardService.getAll():
            print(card)

    def uiRunCrudRezervareMenu(self):
        while True:
            print("1. Adauga rezervare")
            print("2. Sterge rezervare")
            print("3. Modifica rezervare")
            print("a. Afisare rezervari")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiAdaugaRezervare()
            elif optiune == "2":
                self.uiStergeRezervare()
            elif optiune == "3":
                self.uiModificaRezervare()
            elif optiune.lower() == "a":
                self.uiShowallRezervari()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita ! Reincercati")

    def uiAdaugaRezervare(self):
        try:
            idEntitate = input("Dati id-ul rezervarii: ")
            idFilm = input("Dati id-ul filmului: ")
            idCard = input("Dati id-ul cardului: ")
            data = datetime.datetime.strptime(input("Dati data "
                                                    "rezervarii "
                                                    "(DD.MM.YYYY): "),
                                              "%d.%m.%Y")
            dataString = datetime.datetime.strftime(
                data, "%d.%m.%Y")
            ora = datetime.datetime.strptime(input("Dati ora rezervarii"
                                                   " (HH:MM): "), "%H:%M")
            oraString = datetime.datetime.strftime(ora, "%H:%M")
            self.rezervareService.adaugaRezervare(idEntitate, idFilm,
                                                  idCard, dataString,
                                                  oraString)
            if idCard == "0":
                print(f"Nu se primesc puncte pe card.")
            else:
                print(f"Pe cardul {idCard} s-au adaugat "
                      f"{self.rezervareService.acumuleazaPuncte(idFilm)}"
                      f" puncte. "
                      f"Totalul este de "
                      f"{self.cardService.getById(idCard).puncteCumulate}.")
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiStergeRezervare(self):
        try:
            idEntitate = input("Dati id-ul rezervarii pe care doriti"
                               " sa o stergeti: ")
            self.rezervareService.stergeRezervare(idEntitate)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaRezervare(self):
        try:
            idEntitate = input("Dati id-u rezervarii pe care doriti "
                               "sa o modificati: ")
            idFilm = input("Dati noul id al filmului: ")
            idCard = input("Dati noul id al cardului: ")
            data = datetime.datetime.strptime(input("Dati data "
                                                    "rezervarii "
                                                    "(DD.MM.YYYY): "),
                                              "%d.%m.%Y")
            dataString = datetime.datetime.strftime(
                data, "%d.%m.%Y")
            ora = datetime.datetime.strptime(input("Dati ora rezervarii "
                                                   "(HH:MM): "), "%H:%M")
            oraString = datetime.datetime.strftime(ora, "%H:%M")
            self.rezervareService.modificaRezervare(idEntitate, idFilm,
                                                    idCard, dataString,
                                                    oraString)
            if idCard == "0":
                print(f"Nu se primesc puncte pe card.")
            else:
                puncte = self.cardService.getById(idEntitate).puncteCumulate
                print(f"Pe cardul {idCard} s-au adaugat "
                      f"{self.rezervareService.acumuleazaPuncte(idEntitate)}"
                      f" puncte. "
                      f"Totalul este de {puncte}.")
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiShowallRezervari(self):
        for rezervare in self.rezervareService.getAll():
            print(rezervare)

    def uiOrdonareDescCarduriDupaPuncte(self):
        if not self.cardService.ordonareDescCarduriDupaPuncte():
            print("Nu exista carduri pe care sa le afisam !")
        else:
            for card in self.cardService.ordonareDescCarduriDupaPuncte():
                print(card)

    def uiGenereazaFilmeRandom(self):
        try:
            n = int(input("Dati numarul de filme random "
                          "care doriti sa fie generat: "))
            self.filmGenerator.genereazaFilmeRandom(n)
            for film in self.filmGenerator.getAll():
                print(film)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiFunctionalitatiMenu(self):
        while True:
            print("1. Căutare filme și clienți. Căutare full text.")
            print("2. Afișarea tuturor rezervărilor dintr-un "
                  "interval de ore dat, indiferent de zi.")
            print("3. Afișarea filmelor ordonate descrescător după "
                  "numărul de rezervări.")
            print("4. Afișarea cardurilor client ordonate descrescător"
                  " după numărul de puncte de pe card.")
            print("5. Ștergerea tuturor rezervărilor dintr-un"
                  " anumit interval de zile.")
            print("6. Incrementarea cu o valoare dată a "
                  "punctelor de pe toate cardurile "
                  "a căror zi de naștere se află într-un interval dat.")
            print("s. Stergere in cascada (filme).")
            print("r. Genereaza filme random")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                while True:
                    print("1. Cautare filme")
                    print("2. Cautare clienti")
                    print("x. Iesire")
                    opt = input("Dati optiunea: ")
                    if opt == "1":
                        string = input("Dati sirul de caractere pe "
                                       "care doriti sa-l cautati: ")
                        filme = self.filmService.cautareTextFilm(string)
                        if not filme:
                            print("Nu s-au gasit filme !")
                        else:
                            for film in filme:
                                print(film)
                    elif opt == "2":
                        string = input("Dati sirul de caractere pe care "
                                       "doriti sa-l cautati: ")
                        carduri = self.cardService.cautareTextCard(string)
                        if not carduri:
                            print("Nu s-au gasit carduri !")
                        else:
                            for card in carduri:
                                print(card)
                    elif opt.lower() == "x":
                        break
                    else:
                        print("Optiune gresita! Reincercati ")
            elif optiune == "2":
                self.uiAfisareRezervariIntervalOrar()
            elif optiune == "3":
                self.uiOrdonareFilmeDescDupaRezervari()
            elif optiune == "4":
                self.uiOrdonareDescCarduriDupaPuncte()
            elif optiune == "5":
                self.uiStergereRezervariIntervalZile()
            elif optiune == "6":
                self.uiAdaugaValoarePuncte()
            elif optiune.lower() == "s":
                self.uiStergereInCascada()
            elif optiune.lower() == "r":
                self.uiGenereazaFilmeRandom()
            elif optiune.lower() == "x":
                break
            else:
                print("Optiune gresita ! Reincercati ")

    def uiOrdonareFilmeDescDupaRezervari(self):
        if not self.rezervareService.ordonareFilmeDescDupaRezervari():
            print("Nu exista filme de afisat !")
        else:
            for film in self.rezervareService.ordonareFilmeDescDupaRezervari():
                print(film)

    def uiAfisareRezervariIntervalOrar(self):
        try:
            ora1 = datetime.datetime.strptime(input("Dati prima ora: "),
                                              "%H:%M")
            ora2 = datetime.datetime.strptime(input("Dati a doua ora: "),
                                              "%H:%M")
            rezultat = []
            self.rezervareService.\
                afisareRezervariIntervalOrar(ora1, ora2,
                                             self.rezervareService.getAll(),
                                             rezultat)
            if not rezultat:
                print("Nu exista rezervari in intervalul specificat !")
            else:
                for rezervare in rezultat:
                    print(rezervare)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiStergereRezervariIntervalZile(self):
        try:
            data1 = datetime.datetime.strptime(input("Dati prima data: "),
                                               "%d.%m.%Y")
            data2 = datetime.datetime.strptime(input("Dati a doua data: "),
                                               "%d.%m.%Y")
            self.rezervareService.stergereRezervariIntervalZile(data1, data2)
            print("Rezervarile din intervalul specificat au fost sterse !")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiAdaugaValoarePuncte(self):
        try:
            data1 = datetime.datetime.strptime(input("Dati prima data: "),
                                               "%d.%m.%Y")
            data2 = datetime.datetime.strptime(input("Dati a doua data: "),
                                               "%d.%m.%Y")
            valoare = int(input("Dati nr de puncte pe care doriti sa-l "
                                "adaugati "
                                "cardurilor din intervalul specificat: "))
            rezultat = self.cardService.adaugaValoarePuncte(
                data1, data2, valoare)
            if not rezultat:
                print("Nu exista carduri in intervalul specificat !")
            else:
                print(f"Au fost adaugate {valoare} puncte la "
                      f"cardurile a caror"
                      f" zi de nastere se afla in intervalul "
                      f"{data1.date()} - "
                      f"{data2.date()}")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def uiStergereInCascada(self):
        try:
            idFilm = input("Dati id-ul filmului pe"
                           " care doriti sa-l stergeti: ")
            self.rezervareService.stergereInCascada(idFilm)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
