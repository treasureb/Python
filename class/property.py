#! /usr/bin/env
#coding=utf-8

class Account(object):
    """
    账号类
    """
    def __init__(self,rate):
        self.__amt = 0  #本金
        self.rate = rate    #汇率    
    @property
    def amount(self):
        """
        账号余额(美元)
        """
        return self.__amt
    @property
    def cny(self):
        """
        账号余额(人民币)
        """
        return self.__amt*self.rate
    @amount.setter
    def amount(self,value):
        if value < 0:
            print("Sorry,no negative amount in the account.")
            return
        self.__amt = value

if __name__ == '__main__':
    acc = Account(rate=6.6)
    acc.amount = 20
    print("Dollar amount:",acc.amount)
    print("In CNY:",acc.cny)
    acc.amount = -100
    print("Dollar amount:",acc.amount)
