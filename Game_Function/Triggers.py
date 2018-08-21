from enum import Enum


class Trigger(Enum):

    # single digits means

    Ignition = 0
    OnTurnStart = 1
    OnBuildingPhaseEnter = 2
    OnWeatherChange = 3
    OnCreatureBuy = 4
    OnDevelopmentBuy = 5
    OnMagicBuy = 6
    OnCardAct = 7
    Continuous = 8
    assistfromgrave = 9



