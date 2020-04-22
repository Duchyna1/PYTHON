settings = {
    'states': {
        'menu': {
            'window': {
                'title': 'Menu'
            },
            'buttons': {
                'play': {
                    'text': 'PLAY',
                    'font': ("Purisa", 20),
                    'pady': 12,
                    'width': 15,
                    'activebackground': '#afafaf',
                    'bd': 1,
                    'highlightcolor': '#afafaf',
                    'relief': 'solid'
                },
                'tutorial': {
                    'text': 'TUTORIAL',
                    'font': ("Purisa", 20),
                    'pady': 12,
                    'width': 15,
                    'activebackground': '#afafaf',
                    'bd': 1,
                    'highlightcolor': '#afafaf',
                    'relief': 'solid'
                },
                'quit': {
                    'text': 'QUIT',
                    'font': ("Purisa", 20),
                    'pady': 12,
                    'width': 15,
                    'activebackground': '#afafaf',
                    'bd': 1,
                    'highlightcolor': '#afafaf',
                    'relief': 'solid'
                }
            }
        },
        'game': {
            'toWin': 1000,
            'toLose': -100,
            'window': {
                'title': 'GAME'
            },
            'canvas': {
                'width': 400,
                'height': 650
            },
            'pre': {
                'bg': '#000000',
                'text': {
                    'text': 'Click to start',
                    'color': '#ffffff',
                    'font': ("Purisa", 20)
                }
            },
            'game': {
                'bg': '#ffffff',
                'tickSpeed': 10,
                'score': {
                    'missGood': 2,
                    'missBad': 1,
                    'good': 10,
                    'bad': 20
                }
            },
            'pause': {
                'text': {
                    'text': 'Click to continue',
                    'color': '#000000',
                    'font': ("Purisa", 20)
                },
                'rect': {
                    'width': 0,
                    'color': '#7f7f7f'
                },
                'quitButton': {
                    'width': 50,
                    'height': 50,
                    'border': 0,
                    'color': '#afafaf',
                    'text': 'QUIT'
                },
            },
            'score': {
                'text': {
                    'text': {
                        'win': 'You win!',
                        'lose': 'Game over!'
                    },
                    'color': '#000000',
                    'font': ("Purisa", 20)
                },
                'rect': {
                    'width': 0,
                    'color': '#7f7f7f'
                },
                'quitButton': {
                    'width': 100,
                    'height': 50,
                    'border': 1,
                    'color': '#afafaf',
                    'text': 'QUIT'
                },
                'restartButton': {
                    'width':  100,
                    'height': 50,
                    'border': 1,
                    'color':  '#afafaf',
                    'text':   'RESTART'
                },
                'continueButton': {
                    'width':  100,
                    'height': 50,
                    'border': 1,
                    'color':  '#afafaf',
                    'text':   'CONTINUE'
                },
            }
        },
        'tutorial': {
            'window': {
                'title': 'Tutorial'
            },
            'canvas': {
                'bg': '#000000',
                'width': 250,
                'height': 250
            },
            'text': {
                'text':  'Text', # TODO: tutorial text
                'color': '#ffffff',
                'font':  ("Purisa", 20)
            },
            'backButton': {
                'text': 'BACK',
                'font': ("Purisa", 10),
                'pady': 0,
                'width': 30,
                'activebackground': '#afafaf',
                'bd': 0,
                'highlightcolor': '#afafaf',
                'relief': 'solid'
            }
        }
    },
    'ball': {
        'r': 4,
        'width': 2,
        'g': 5,
        'offset': 200,
        'color': {
            'good': '#ffffff',
            'bad': '#000000'
        }
    },
    'paddle': {
        'width': 75,
        'height': 20,
        'h': 20,
        'color': {
            'good': '#ffffff',
            'bad': '#000000'
        },
        'border': 5
    }
}

def setG(g):
    settings['ball']['g'] = g