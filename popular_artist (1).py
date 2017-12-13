import plotly
import plotly.plotly as py
import plotly.graph_objs as go
def main():
    data = [go.Bar(
            y = [9, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            x = ['Drake', 'The Weeknd', 'Ariana Grande', 'Shawn Mendes', 'The Chainsmokers', 'Adele', 'Alessia Cara'\
                 'Bryson Tiller', 'DJ Khaled', 'Fetty Wap', 'Florida Georgia Line', 'Kanye West'\
                 'Keith Urban', 'Luke Bryan', 'Major Lazer', 'Meghan Trainor', 'Rihanna', 'Selena Gomez',\
                 'Twenty one pilots'])]
    plotly.offline.plot(data)
main()
