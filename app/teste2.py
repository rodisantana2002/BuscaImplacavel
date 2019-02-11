import teste1 as t
import scihub as sci


# carrega script e roda em modo força-bruta
def main():
    td = t.voar()
    sc = sci.SciHub()
    td.save()

if __name__ == '__main__':
    main()
