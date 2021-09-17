#!/usr/bin/python
# -*- encoding: utf-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2021, 10, 12)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True
  def clear():
(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-vendors"], {
    "010e": function(t, e, n) {
        (function(t, e) {
            e(n("c1df"))
        }
        )(0, (function(t) {
            "use strict";
            //! moment.js locale configuration
            var e = t.defineLocale("uz-latn", {
                months: "Yanvar_Fevral_Mart_Aprel_May_Iyun_Iyul_Avgust_Sentabr_Oktabr_Noyabr_Dekabr".split("_"),
                monthsShort: "Yan_Fev_Mar_Apr_May_Iyun_Iyul_Avg_Sen_Okt_Noy_Dek".split("_"),
                weekdays: "Yakshanba_Dushanba_Seshanba_Chorshanba_Payshanba_Juma_Shanba".split("_"),
                weekdaysShort: "Yak_Dush_Sesh_Chor_Pay_Jum_Shan".split("_"),
                weekdaysMin: "Ya_Du_Se_Cho_Pa_Ju_Sha".split("_"),
                longDateFormat: {
                    LT: "HH:mm",
                    LTS: "HH:mm:ss",
                    L: "DD/MM/YYYY",
                    LL: "D MMMM YYYY",
                    LLL: "D MMMM YYYY HH:mm",
                    LLLL: "D MMMM YYYY, dddd HH:mm"
                },
                calendar: {
                    sameDay: "[Bugun soat] LT [da]",
                    nextDay: "[Ertaga] LT [da]",
                    nextWeek: "dddd [kuni soat] LT [da]",
                    lastDay: "[Kecha soat] LT [da]",
                    lastWeek: "[O'tgan] dddd [kuni soat] LT [da]",
                    sameElse: "L"
                },
                relativeTime: {
                    future: "Yaqin %s ichida",
                    past: "Bir necha %s oldin",
                    s: "soniya",
                    ss: "%d soniya",
                    m: "bir daqiqa",
                    mm: "%d daqiqa",
                    h: "bir soat",
                    hh: "%d soat",
                    d: "bir kun",
                    dd: "%d kun",
                    M: "bir oy",
                    MM: "%d oy",
                    y: "bir yil",
                    yy: "%d yil"
                },
                week: {
                    dow: 1,
                    doy: 7
                }
            });
            return e
        }
        ))
    },
    "01f9": function(t, e, n) {
        "use strict";
        var i = n("2d00")
          , s = n("5ca1")
          , r = n("2aba")
          , a = n("32e9")
          , o = n("84f2")
          , u = n("41a0")
          , c = n("7f20")
          , l = n("38fd")
          , d = n("2b4c")("iterator")
          , h = !([].keys && "next"in [].keys())
          , f = "@@iterator"
          , m = "keys"
          , p = "values"
          , v = function() {
            return this
        };
        t.exports = function(t, e, n, _, g, y, b) {
            u(n, e, _);
            var M, w, k, x = function(t) {
                if (!h && t in D)
                    return D[t];
                switch (t) {
                case m:
                    return function() {
                        return new n(this,t)
                    }
                    ;
                case p:
                    return function() {
                        return new n(this,t)
                    }
                }
                return function() {
                    return new n(this,t)
                }
            }, L = e + " Iterator", T = g == p, S = !1, D = t.prototype, Y = D[d] || D[f] || g && D[g], O = Y || x(g), C = g ? T ? x("entries") : O : void 0, j = "Array" == e && D.entries || Y;
            if (j && (k = l(j.call(new t)),
            k !== Object.prototype && k.next && (c(k, L, !0),
            i || "function" == typeof k[d] || a(k, d, v))),
            T && Y && Y.name !== p && (S = !0,
            O = function() {
                return Y.call(this)
            }
            ),
            i && !b || !h && !S && D[d] || a(D, d, O),
            o[e] = O,
            o[L] = v,
            g)
                if (M = {
                    values: T ? O : x(p),
                    keys: y ? O : x(m),
                    entries: C
                },
                b)
                    for (w in M)
                        w in D || r(D, w, M[w]);
                else
                    s(s.P + s.F * (h || S), e, M);
            return M
        }
    },
    "02f4": function(t, e, n) {
        var i = n("4588")
          , s = n("be13");
        t.exports = function(t) {
            return function(e, n) {
                var r, a, o = String(s(e)), u = i(n), c = o.length;
                return u < 0 || u >= c ? t ? "" : void 0 : (r = o.charCodeAt(u),
                r < 55296 || r > 56319 || u + 1 === c || (a = o.charCodeAt(u + 1)) < 56320 || a > 57343 ? t ? o.charAt(u) : r : t ? o.slice(u, u + 2) : a - 56320 + (r - 55296 << 10) + 65536)
            }
        }
    },
    "02fb": function(t, e, n) {
        (function(t, e) {
            e(n("c1df"))
        }
        
        if current in numbers:
                    print(newperiod+1,": RED")
                else:
                    print(newperiod+1,": GREEN")
            else:
                if current in numbers:
                    print(newperiod+1,": GREEN")
                else:
                    print(newperiod+1,": RED")
        i=i+1
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
