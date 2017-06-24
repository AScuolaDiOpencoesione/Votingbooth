from __future__ import unicode_literals
from __future__ import division

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Avg
# Create your models here.
import json

itms = {1:[
{"ID_ASOC":1, "livello":5, "klout":	3.912	, "crit_D": 8.91, "penalty":0},
{"ID_ASOC":10, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":-5},
{"ID_ASOC":103, "livello":1, "klout":	0	, "crit_D": 1.00, "penalty":0},
{"ID_ASOC":105, "livello":2, "klout":	0	, "crit_D": 2.00, "penalty":-5},
{"ID_ASOC":110, "livello":2, "klout":	0	, "crit_D": 2.00, "penalty":0},
{"ID_ASOC":111, "livello":4, "klout":	0	, "crit_D": 4.00, "penalty":0},
{"ID_ASOC":113, "livello":3, "klout":	3.133333333	, "crit_D": 6.13, "penalty":0},
{"ID_ASOC":116, "livello":5, "klout":	2.866666667	, "crit_D": 7.87, "penalty":0},
{"ID_ASOC":118, "livello":5, "klout":	4.733333333	, "crit_D": 9.73, "penalty":0},
{"ID_ASOC":119, "livello":5, "klout":	4.448	, "crit_D": 9.45, "penalty":0},
{"ID_ASOC":130, "livello":5, "klout":	4.022222222	, "crit_D": 9.02, "penalty":0},
{"ID_ASOC":133, "livello":5, "klout":	4.288888889	, "crit_D": 9.29, "penalty":0},
{"ID_ASOC":135, "livello":5, "klout":	1	, "crit_D": 6.00, "penalty":0},
{"ID_ASOC":136, "livello":4, "klout":	3.843555556	, "crit_D": 7.84, "penalty":0},
{"ID_ASOC":137, "livello":4, "klout":	4.644444444	, "crit_D": 8.64, "penalty":0},
{"ID_ASOC":14, "livello":5, "klout":	2.955555556	, "crit_D": 7.96, "penalty":0},
{"ID_ASOC":140, "livello":5, "klout":	0	, "crit_D": 5.00, "penalty":0},
{"ID_ASOC":141, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":0},
{"ID_ASOC":144, "livello":5, "klout":	4.022222222	, "crit_D": 9.02, "penalty":0},
{"ID_ASOC":146, "livello":2, "klout":	0	, "crit_D": 2.00, "penalty":-10},
{"ID_ASOC":149, "livello":5, "klout":	3.755555556	, "crit_D": 8.76, "penalty":0},
{"ID_ASOC":15, "livello":5, "klout":	0	, "crit_D": 5.00, "penalty":0},
{"ID_ASOC":152, "livello":3, "klout":	3.579555556	, "crit_D": 6.58, "penalty":0},
{"ID_ASOC":156, "livello":5, "klout":	3.933333333	, "crit_D": 8.93, "penalty":0},
{"ID_ASOC":16, "livello":4, "klout":	4.733333333	, "crit_D": 8.73, "penalty":0},
{"ID_ASOC":160, "livello":1, "klout":	0	, "crit_D": 1.00, "penalty":0},
{"ID_ASOC":164, "livello":5, "klout":	2.603555556	, "crit_D": 7.60, "penalty":0},
{"ID_ASOC":165, "livello":4, "klout":	0	, "crit_D": 4.00, "penalty":-10},
{"ID_ASOC":168, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":0},
{"ID_ASOC":169, "livello":4, "klout":	5	, "crit_D": 9.00, "penalty":0},
{"ID_ASOC":18, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":0},
{"ID_ASOC":181, "livello":3, "klout":	3.044444444	, "crit_D": 6.04, "penalty":-5},
{"ID_ASOC":2, "livello":4, "klout":	3.755555556	, "crit_D": 7.76, "penalty":0},
{"ID_ASOC":23, "livello":5, "klout":	4.466666667	, "crit_D": 9.47, "penalty":0},
{"ID_ASOC":24, "livello":5, "klout":	4.804444444	, "crit_D": 9.80, "penalty":0},
{"ID_ASOC":30, "livello":5, "klout":	0	, "crit_D": 5.00, "penalty":0},
{"ID_ASOC":31, "livello":5, "klout":	0	, "crit_D": 5.00, "penalty":0},
{"ID_ASOC":35, "livello":5, "klout":	4.288888889	, "crit_D": 9.29, "penalty":0},
{"ID_ASOC":36, "livello":5, "klout":	3.755555556	, "crit_D": 8.76, "penalty":0},
{"ID_ASOC":37, "livello":4, "klout":	2.097777778	, "crit_D": 6.10, "penalty":0},
{"ID_ASOC":38, "livello":5, "klout":	0	, "crit_D": 5.00, "penalty":-5},
{"ID_ASOC":4, "livello":4, "klout":	4.672	, "crit_D": 8.67, "penalty":0},
{"ID_ASOC":42, "livello":5, "klout":	2.6	, "crit_D": 7.60, "penalty":0},
{"ID_ASOC":43, "livello":5, "klout":	4.111111111	, "crit_D": 9.11, "penalty":0},
{"ID_ASOC":44, "livello":3, "klout":	3.933333333	, "crit_D": 6.93, "penalty":0},
{"ID_ASOC":45, "livello":4, "klout":	4.012444444	, "crit_D": 8.01, "penalty":0},
{"ID_ASOC":5, "livello":5, "klout":	4.424	, "crit_D": 9.42, "penalty":0},
{"ID_ASOC":50, "livello":5, "klout":	3.044444444	, "crit_D": 8.04, "penalty":0},
{"ID_ASOC":52, "livello":4, "klout":	0	, "crit_D": 4.00, "penalty":-5},
{"ID_ASOC":54, "livello":5, "klout":	4.644444444	, "crit_D": 9.64, "penalty":0},
{"ID_ASOC":56, "livello":3, "klout":	3.933333333	, "crit_D": 6.93, "penalty":0},
{"ID_ASOC":62, "livello":5, "klout":	4.555555556	, "crit_D": 9.56, "penalty":0},
{"ID_ASOC":63, "livello":1, "klout":	0	, "crit_D": 1.00, "penalty":0},
{"ID_ASOC":65, "livello":5, "klout":	4.377777778	, "crit_D": 9.38, "penalty":0},
{"ID_ASOC":66, "livello":3, "klout":	2.511111111	, "crit_D": 5.51, "penalty":0},
{"ID_ASOC":67, "livello":5, "klout":	0	, "crit_D": 5.00, "penalty":0},
{"ID_ASOC":68, "livello":5, "klout":	0	, "crit_D": 5.00, "penalty":0},
{"ID_ASOC":69, "livello":4, "klout":	4.056	, "crit_D": 8.06, "penalty":0},
{"ID_ASOC":70, "livello":5, "klout":	3.4	, "crit_D": 8.40, "penalty":0},
{"ID_ASOC":71, "livello":5, "klout":	4.111111111	, "crit_D": 9.11, "penalty":0},
{"ID_ASOC":75, "livello":4, "klout":	4.555555556	, "crit_D": 8.56, "penalty":0},
{"ID_ASOC":78, "livello":4, "klout":	1	, "crit_D": 5.00, "penalty":0},
{"ID_ASOC":80, "livello":4, "klout":	4.377777778	, "crit_D": 8.38, "penalty":-10},
{"ID_ASOC":83, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":0},
{"ID_ASOC":84, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":0},
{"ID_ASOC":86, "livello":5, "klout":	4.111111111	, "crit_D": 9.11, "penalty":0},
{"ID_ASOC":87, "livello":4, "klout":	3.902222222	, "crit_D": 7.90, "penalty":0},
{"ID_ASOC":88, "livello":3, "klout":	1.444444444	, "crit_D": 4.44, "penalty":0},
{"ID_ASOC":9, "livello":5, "klout":	1.8	, "crit_D": 6.80, "penalty":0},
{"ID_ASOC":91, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":0},
{"ID_ASOC":92, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":0},
{"ID_ASOC":94, "livello":5, "klout":	3.844444444	, "crit_D": 8.84, "penalty":0},
{"ID_ASOC":95, "livello":3, "klout":	0	, "crit_D": 3.00, "penalty":-5},
{"ID_ASOC":97, "livello":5, "klout":	2.356444444	, "crit_D": 7.36, "penalty":0} 
], 
2:[
  {
    "ID_ASOC": 5,
    "crit_D": 7
  },
  {
    "ID_ASOC": 6,
    "crit_D": 8
  },
  {
    "ID_ASOC": 7,
    "crit_D": 9.8
  },
  {
    "ID_ASOC": 9,
    "crit_D": 9.64
  },
  {
    "ID_ASOC": 10,
    "crit_D": 9.72
  },
  {
    "ID_ASOC": 11,
    "crit_D": 7.64
  },
  {
    "ID_ASOC": 13,
    "crit_D": 8.96
  },
  {
    "ID_ASOC": 15,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 16,
    "crit_D": 8.32
  },
  {
    "ID_ASOC": 17,
    "crit_D": 8.8
  },
  {
    "ID_ASOC": 18,
    "crit_D": 7.84
  },
  {
    "ID_ASOC": 21,
    "crit_D": 8.72
  },
  {
    "ID_ASOC": 23,
    "crit_D": 6.16
  },
  {
    "ID_ASOC": 24,
    "crit_D": 8.08
  },
  {
    "ID_ASOC": 25,
    "crit_D": 3
  },
  {
    "ID_ASOC": 26,
    "crit_D": 3.48
  },
  {
    "ID_ASOC": 31,
    "crit_D": 8.7
  },
  {
    "ID_ASOC": 34,
    "crit_D": 7.2
  },
  {
    "ID_ASOC": 36,
    "crit_D": 8.52
  },
  {
    "ID_ASOC": 39,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 42,
    "crit_D": 8.84
  },
  {
    "ID_ASOC": 44,
    "crit_D": 7.84
  },
  {
    "ID_ASOC": 46,
    "crit_D": 8.49
  },
  {
    "ID_ASOC": 48,
    "crit_D": 7
  },
  {
    "ID_ASOC": 49,
    "crit_D": 5.12
  },
  {
    "ID_ASOC": 52,
    "crit_D": 7
  },
  {
    "ID_ASOC": 55,
    "crit_D": 9.68
  },
  {
    "ID_ASOC": 56,
    "crit_D": 9.37
  },
  {
    "ID_ASOC": 57,
    "crit_D": 6.32
  },
  {
    "ID_ASOC": 58,
    "crit_D": 4
  },
  {
    "ID_ASOC": 59,
    "crit_D": 7.84
  },
  {
    "ID_ASOC": 60,
    "crit_D": 9.52
  },
  {
    "ID_ASOC": 61,
    "crit_D": 9.4
  },
  {
    "ID_ASOC": 64,
    "crit_D": 7.15
  },
  {
    "ID_ASOC": 65,
    "crit_D": 6
  },
  {
    "ID_ASOC": 66,
    "crit_D": 6.28
  },
  {
    "ID_ASOC": 67,
    "crit_D": 9.2
  },
  {
    "ID_ASOC": 68,
    "crit_D": 7.56
  },
  {
    "ID_ASOC": 69,
    "crit_D": 9.08
  },
  {
    "ID_ASOC": 70,
    "crit_D": 8
  },
  {
    "ID_ASOC": 71,
    "crit_D": 9.89
  },
  {
    "ID_ASOC": 72,
    "crit_D": 5.28
  },
  {
    "ID_ASOC": 73,
    "crit_D": 9.36
  },
  {
    "ID_ASOC": 74,
    "crit_D": 4.16
  },
  {
    "ID_ASOC": 75,
    "crit_D": 10
  },
  {
    "ID_ASOC": 76,
    "crit_D": 8.24
  },
  {
    "ID_ASOC": 78,
    "crit_D": 5
  },
  {
    "ID_ASOC": 79,
    "crit_D": 9.32
  },
  {
    "ID_ASOC": 80,
    "crit_D": 4.12
  },
  {
    "ID_ASOC": 81,
    "crit_D": 9.04
  },
  {
    "ID_ASOC": 82,
    "crit_D": 7.4
  },
  {
    "ID_ASOC": 83,
    "crit_D": 9.38
  },
  {
    "ID_ASOC": 84,
    "crit_D": 8.4
  },
  {
    "ID_ASOC": 87,
    "crit_D": 6.2
  },
  {
    "ID_ASOC": 88,
    "crit_D": 7
  },
  {
    "ID_ASOC": 90,
    "crit_D": 8.73
  },
  {
    "ID_ASOC": 91,
    "crit_D": 8.68
  },
  {
    "ID_ASOC": 95,
    "crit_D": 9.57
  },
  {
    "ID_ASOC": 96,
    "crit_D": 8.44
  },
  {
    "ID_ASOC": 98,
    "crit_D": 3
  },
  {
    "ID_ASOC": 99,
    "crit_D": 7.24
  },
  {
    "ID_ASOC": 100,
    "crit_D": 9.56
  },
  {
    "ID_ASOC": 102,
    "crit_D": 5
  },
  {
    "ID_ASOC": 105,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 109,
    "crit_D": 6.64
  },
  {
    "ID_ASOC": 110,
    "crit_D": 9.64
  },
  {
    "ID_ASOC": 111,
    "crit_D": 6
  },
  {
    "ID_ASOC": 112,
    "crit_D": 7
  },
  {
    "ID_ASOC": 116,
    "crit_D": 9.44
  },
  {
    "ID_ASOC": 117,
    "crit_D": 6.51
  },
  {
    "ID_ASOC": 118,
    "crit_D": 9.76
  },
  {
    "ID_ASOC": 119,
    "crit_D": 9.61
  },
  {
    "ID_ASOC": 120,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 121,
    "crit_D": 9.12
  },
  {
    "ID_ASOC": 122,
    "crit_D": 4.24
  },
  {
    "ID_ASOC": 125,
    "crit_D": 9.36
  },
  {
    "ID_ASOC": 126,
    "crit_D": 8.64
  },
  {
    "ID_ASOC": 132,
    "crit_D": 7
  },
  {
    "ID_ASOC": 134,
    "crit_D": 6.36
  },
  {
    "ID_ASOC": 135,
    "crit_D": 8.48
  },
  {
    "ID_ASOC": 136,
    "crit_D": 3.32
  },
  {
    "ID_ASOC": 137,
    "crit_D": 6
  },
  {
    "ID_ASOC": 138,
    "crit_D": 3
  },
  {
    "ID_ASOC": 139,
    "crit_D": 9.28
  },
  {
    "ID_ASOC": 140,
    "crit_D": 6.32
  },
  {
    "ID_ASOC": 144,
    "crit_D": 9.72
  },
  {
    "ID_ASOC": 145,
    "crit_D": 8.96
  },
  {
    "ID_ASOC": 149,
    "crit_D": 6.72
  },
  {
    "ID_ASOC": 151,
    "crit_D": 9.52
  },
  {
    "ID_ASOC": 152,
    "crit_D": 7.54
  },
  {
    "ID_ASOC": 154,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 156,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 159,
    "crit_D": 7.28
  },
  {
    "ID_ASOC": 160,
    "crit_D": 7.79
  },
  {
    "ID_ASOC": 164,
    "crit_D": 2
  },
  {
    "ID_ASOC": 167,
    "crit_D": 7.12
  },
  {
    "ID_ASOC": 168,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 169,
    "crit_D": 8.8
  },
  {
    "ID_ASOC": 170,
    "crit_D": 2
  },
  {
    "ID_ASOC": 172,
    "crit_D": 4
  },
  {
    "ID_ASOC": 174,
    "crit_D": 7.4
  },
  {
    "ID_ASOC": 177,
    "crit_D": 8
  },
  {
    "ID_ASOC": 179,
    "crit_D": 8.72
  },
  {
    "ID_ASOC": 180,
    "crit_D": 7.32
  },
  {
    "ID_ASOC": 182,
    "crit_D": 7.36
  },
  {
    "ID_ASOC": 183,
    "crit_D": 5.92
  },
  {
    "ID_ASOC": 184,
    "crit_D": 2
  },
  {
    "ID_ASOC": 185,
    "crit_D": 4.12
  },
  {
    "ID_ASOC": 186,
    "crit_D": 8
  },
  {
    "ID_ASOC": 187,
    "crit_D": 6.44
  },
  {
    "ID_ASOC": 188,
    "crit_D": 6
  },
  {
    "ID_ASOC": 192,
    "crit_D": 8.08
  },
  {
    "ID_ASOC": 193,
    "crit_D": 9.32
  },
  {
    "ID_ASOC": 194,
    "crit_D": 5
  },
  {
    "ID_ASOC": 195,
    "crit_D": 7
  },
  {
    "ID_ASOC": 197,
    "crit_D": 5
  },
  {
    "ID_ASOC": 198,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 199,
    "crit_D": 6.11
  },
  {
    "ID_ASOC": 200,
    "crit_D": 7.36
  },
  {
    "ID_ASOC": 202,
    "crit_D": 4.68
  },
  {
    "ID_ASOC": 205,
    "crit_D": 7.72
  },
  {
    "ID_ASOC": 206,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 207,
    "crit_D": 8.68
  },
  {
    "ID_ASOC": 208,
    "crit_D": 8.9
  },
  {
    "ID_ASOC": 209,
    "crit_D": 6
  },
  {
    "ID_ASOC": 211,
    "crit_D": 7.48
  },
  {
    "ID_ASOC": 213,
    "crit_D": 7.33
  },
  {
    "ID_ASOC": 216,
    "crit_D": 8.4
  },
  {
    "ID_ASOC": 218,
    "crit_D": 3.48
  },
  {
    "ID_ASOC": 220,
    "crit_D": 9.58
  },
  {
    "ID_ASOC": 222,
    "crit_D": 3
  },
  {
    "ID_ASOC": 224,
    "crit_D": 4.12
  },
  {
    "ID_ASOC": 228,
    "crit_D": 6.32
  },
  {
    "ID_ASOC": 230,
    "crit_D": 6.64
  },
  {
    "ID_ASOC": 231,
    "crit_D": 6
  },
  {
    "ID_ASOC": 232,
    "crit_D": 9.8
  },
  {
    "ID_ASOC": 234,
    "crit_D": 7.12
  },
  {
    "ID_ASOC": 238,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 240,
    "crit_D": 8.6
  }
],
3:[
  {
    "ID_ASOC": 5,
    "crit_D": 7
  },
  {
    "ID_ASOC": 6,
    "crit_D": 8
  },
  {
    "ID_ASOC": 7,
    "crit_D": 9.8
  },
  {
    "ID_ASOC": 9,
    "crit_D": 9.64
  },
  {
    "ID_ASOC": 10,
    "crit_D": 9.72
  },
  {
    "ID_ASOC": 11,
    "crit_D": 7.64
  },
  {
    "ID_ASOC": 13,
    "crit_D": 8.96
  },
  {
    "ID_ASOC": 15,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 16,
    "crit_D": 8.32
  },
  {
    "ID_ASOC": 17,
    "crit_D": 8.8
  },
  {
    "ID_ASOC": 18,
    "crit_D": 7.84
  },
  {
    "ID_ASOC": 21,
    "crit_D": 8.72
  },
  {
    "ID_ASOC": 23,
    "crit_D": 6.16
  },
  {
    "ID_ASOC": 24,
    "crit_D": 8.08
  },
  {
    "ID_ASOC": 25,
    "crit_D": 3
  },
  {
    "ID_ASOC": 26,
    "crit_D": 3.48
  },
  {
    "ID_ASOC": 31,
    "crit_D": 8.7
  },
  {
    "ID_ASOC": 34,
    "crit_D": 7.2
  },
  {
    "ID_ASOC": 36,
    "crit_D": 8.52
  },
  {
    "ID_ASOC": 39,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 42,
    "crit_D": 8.84
  },
  {
    "ID_ASOC": 44,
    "crit_D": 7.84
  },
  {
    "ID_ASOC": 46,
    "crit_D": 8.49
  },
  {
    "ID_ASOC": 48,
    "crit_D": 7
  },
  {
    "ID_ASOC": 49,
    "crit_D": 5.12
  },
  {
    "ID_ASOC": 52,
    "crit_D": 7
  },
  {
    "ID_ASOC": 55,
    "crit_D": 9.68
  },
  {
    "ID_ASOC": 56,
    "crit_D": 9.37
  },
  {
    "ID_ASOC": 57,
    "crit_D": 6.32
  },
  {
    "ID_ASOC": 58,
    "crit_D": 4
  },
  {
    "ID_ASOC": 59,
    "crit_D": 7.84
  },
  {
    "ID_ASOC": 60,
    "crit_D": 9.52
  },
  {
    "ID_ASOC": 61,
    "crit_D": 9.4
  },
  {
    "ID_ASOC": 64,
    "crit_D": 7.15
  },
  {
    "ID_ASOC": 65,
    "crit_D": 6
  },
  {
    "ID_ASOC": 66,
    "crit_D": 6.28
  },
  {
    "ID_ASOC": 67,
    "crit_D": 9.2
  },
  {
    "ID_ASOC": 68,
    "crit_D": 7.56
  },
  {
    "ID_ASOC": 69,
    "crit_D": 9.08
  },
  {
    "ID_ASOC": 70,
    "crit_D": 8
  },
  {
    "ID_ASOC": 71,
    "crit_D": 9.89
  },
  {
    "ID_ASOC": 72,
    "crit_D": 5.28
  },
  {
    "ID_ASOC": 73,
    "crit_D": 9.36
  },
  {
    "ID_ASOC": 74,
    "crit_D": 4.16
  },
  {
    "ID_ASOC": 75,
    "crit_D": 10
  },
  {
    "ID_ASOC": 76,
    "crit_D": 8.24
  },
  {
    "ID_ASOC": 78,
    "crit_D": 5
  },
  {
    "ID_ASOC": 79,
    "crit_D": 9.32
  },
  {
    "ID_ASOC": 80,
    "crit_D": 4.12
  },
  {
    "ID_ASOC": 81,
    "crit_D": 9.04
  },
  {
    "ID_ASOC": 82,
    "crit_D": 7.4
  },
  {
    "ID_ASOC": 83,
    "crit_D": 9.38
  },
  {
    "ID_ASOC": 84,
    "crit_D": 8.4
  },
  {
    "ID_ASOC": 87,
    "crit_D": 6.2
  },
  {
    "ID_ASOC": 88,
    "crit_D": 7
  },
  {
    "ID_ASOC": 90,
    "crit_D": 8.73
  },
  {
    "ID_ASOC": 91,
    "crit_D": 8.68
  },
  {
    "ID_ASOC": 95,
    "crit_D": 9.57
  },
  {
    "ID_ASOC": 96,
    "crit_D": 8.44
  },
  {
    "ID_ASOC": 98,
    "crit_D": 3
  },
  {
    "ID_ASOC": 99,
    "crit_D": 7.24
  },
  {
    "ID_ASOC": 100,
    "crit_D": 9.56
  },
  {
    "ID_ASOC": 102,
    "crit_D": 5
  },
  {
    "ID_ASOC": 105,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 109,
    "crit_D": 6.64
  },
  {
    "ID_ASOC": 110,
    "crit_D": 9.64
  },
  {
    "ID_ASOC": 111,
    "crit_D": 6
  },
  {
    "ID_ASOC": 112,
    "crit_D": 7
  },
  {
    "ID_ASOC": 116,
    "crit_D": 9.44
  },
  {
    "ID_ASOC": 117,
    "crit_D": 6.51
  },
  {
    "ID_ASOC": 118,
    "crit_D": 9.76
  },
  {
    "ID_ASOC": 119,
    "crit_D": 9.61
  },
  {
    "ID_ASOC": 120,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 121,
    "crit_D": 9.12
  },
  {
    "ID_ASOC": 122,
    "crit_D": 4.24
  },
  {
    "ID_ASOC": 125,
    "crit_D": 9.36
  },
  {
    "ID_ASOC": 126,
    "crit_D": 8.64
  },
  {
    "ID_ASOC": 132,
    "crit_D": 7
  },
  {
    "ID_ASOC": 134,
    "crit_D": 6.36
  },
  {
    "ID_ASOC": 135,
    "crit_D": 8.48
  },
  {
    "ID_ASOC": 136,
    "crit_D": 3.32
  },
  {
    "ID_ASOC": 137,
    "crit_D": 6
  },
  {
    "ID_ASOC": 138,
    "crit_D": 3
  },
  {
    "ID_ASOC": 139,
    "crit_D": 9.28
  },
  {
    "ID_ASOC": 140,
    "crit_D": 6.32
  },
  {
    "ID_ASOC": 144,
    "crit_D": 9.72
  },
  {
    "ID_ASOC": 145,
    "crit_D": 8.96
  },
  {
    "ID_ASOC": 149,
    "crit_D": 6.72
  },
  {
    "ID_ASOC": 151,
    "crit_D": 9.52
  },
  {
    "ID_ASOC": 152,
    "crit_D": 7.54
  },
  {
    "ID_ASOC": 154,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 156,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 159,
    "crit_D": 7.28
  },
  {
    "ID_ASOC": 160,
    "crit_D": 7.79
  },
  {
    "ID_ASOC": 164,
    "crit_D": 2
  },
  {
    "ID_ASOC": 167,
    "crit_D": 7.12
  },
  {
    "ID_ASOC": 168,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 169,
    "crit_D": 8.8
  },
  {
    "ID_ASOC": 170,
    "crit_D": 2
  },
  {
    "ID_ASOC": 172,
    "crit_D": 4
  },
  {
    "ID_ASOC": 174,
    "crit_D": 7.4
  },
  {
    "ID_ASOC": 177,
    "crit_D": 8
  },
  {
    "ID_ASOC": 179,
    "crit_D": 8.72
  },
  {
    "ID_ASOC": 180,
    "crit_D": 7.32
  },
  {
    "ID_ASOC": 182,
    "crit_D": 7.36
  },
  {
    "ID_ASOC": 183,
    "crit_D": 5.92
  },
  {
    "ID_ASOC": 184,
    "crit_D": 2
  },
  {
    "ID_ASOC": 185,
    "crit_D": 4.12
  },
  {
    "ID_ASOC": 186,
    "crit_D": 8
  },
  {
    "ID_ASOC": 187,
    "crit_D": 6.44
  },
  {
    "ID_ASOC": 188,
    "crit_D": 6
  },
  {
    "ID_ASOC": 192,
    "crit_D": 8.08
  },
  {
    "ID_ASOC": 193,
    "crit_D": 9.32
  },
  {
    "ID_ASOC": 194,
    "crit_D": 5
  },
  {
    "ID_ASOC": 195,
    "crit_D": 7
  },
  {
    "ID_ASOC": 197,
    "crit_D": 5
  },
  {
    "ID_ASOC": 198,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 199,
    "crit_D": 6.11
  },
  {
    "ID_ASOC": 200,
    "crit_D": 7.36
  },
  {
    "ID_ASOC": 202,
    "crit_D": 4.68
  },
  {
    "ID_ASOC": 205,
    "crit_D": 7.72
  },
  {
    "ID_ASOC": 206,
    "crit_D": 6.12
  },
  {
    "ID_ASOC": 207,
    "crit_D": 8.68
  },
  {
    "ID_ASOC": 208,
    "crit_D": 8.9
  },
  {
    "ID_ASOC": 209,
    "crit_D": 6
  },
  {
    "ID_ASOC": 211,
    "crit_D": 7.48
  },
  {
    "ID_ASOC": 213,
    "crit_D": 7.33
  },
  {
    "ID_ASOC": 216,
    "crit_D": 8.4
  },
  {
    "ID_ASOC": 218,
    "crit_D": 3.48
  },
  {
    "ID_ASOC": 220,
    "crit_D": 9.58
  },
  {
    "ID_ASOC": 222,
    "crit_D": 3
  },
  {
    "ID_ASOC": 224,
    "crit_D": 4.12
  },
  {
    "ID_ASOC": 228,
    "crit_D": 6.32
  },
  {
    "ID_ASOC": 230,
    "crit_D": 6.64
  },
  {
    "ID_ASOC": 231,
    "crit_D": 6
  },
  {
    "ID_ASOC": 232,
    "crit_D": 9.8
  },
  {
    "ID_ASOC": 234,
    "crit_D": 7.12
  },
  {
    "ID_ASOC": 238,
    "crit_D": 8.12
  },
  {
    "ID_ASOC": 240,
    "crit_D": 8.6
  }
]

	}

class VotingSession(models.Model):
	name = models.CharField(max_length=200)
	enabled = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class VotingElement(models.Model):
	session = models.ForeignKey(VotingSession)
	name = models.CharField(max_length=200)
	repr = models.CharField(max_length=1000)
	field = models.CharField(max_length=200, default="ID_ASOC")
	order = models.IntegerField()

	def __str__(self):
		return self.name + " " + self.repr

	def total_vote(self, session_id):
		crit_d = 0
		penalty = 0
		for i in itms.get(self.session_id, []):
			if i.get("ID_ASOC") == int(self.name):
				crit_d = i.get("crit_D")
				penalty = float(i.get("penalty", 0))
		vc = VoteCast.objects.filter(element =self, item__session__id=session_id).aggregate(Sum("vote"))["vote__sum"] or 0
		ve = max(0.000000001, VoterElements.objects.filter(items=self).count())
		
		return (float(vc)/float(ve))+round(float(crit_d),2)+float(penalty)

	def extras(self):
		x = 0
		for i in itms.get(self.session_id, []):
			if i.get("ID_ASOC") == int(self.name):
				#print i
				x = i.get("crit_D")
				x = round(x,2)
		return x


	def penalty(self):
		x = 0
		for i in itms.get(self.session_id):
			if i.get("ID_ASOC") == int(self.name):
				print i
				x = i.get("penalty",0)
				x = round(x,2)
		return x
		
	def extras_stirng(self):
		x = 0
		for i in itms.get(self.session_id):
			if i.get("ID_ASOC") == int(self.name):
				print i
				x = json.dumps(i)
		return x


class VotingItem(models.Model):
	session = models.ForeignKey(VotingSession)
	iframe = models.URLField()
	order = models.IntegerField()
	name = models.CharField(max_length=200)
	description = models.TextField(default="", blank=True)

	def __str__(self):
		return self.name


class VoteCast(models.Model):
	session = models.ForeignKey(VotingSession)
	datetime = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)
	element = models.ForeignKey(VotingElement)
	item = models.ForeignKey(VotingItem)
	vote = models.IntegerField()

	class Meta:
		unique_together = ["session","user","element","item"]


	def __str__(self):
		return "%s - %s - %s - %s" % (self.user.username, self.item, self.element.repr, self.vote, )

class VoterElements(models.Model):
	voter = models.ForeignKey(User, related_name="votes")
	items = models.ManyToManyField(VotingElement, related_name="voters", null=True, blank=True)
	sequence = models.TextField()

	def __str__(self):
		return self.voter.username +" ("+ str(self.items.count()) +")"

	def create_sequence(self):
		self.sequence = schools = [{"item":i.id,"element":e.id, "vote":get_vote(e,i,voter)} for i in VotingItem.objects.filter(session_id = session_id) for e in VoterElements.objects.get(voter=voter).items.all()]

def get_vote(el, itm, voter):
	vc = VoteCast.objects.filter(user = voter, element = el, item=itm)
	if vc.count() > 0:
		return vc.first().vote.id
	else:
		return None