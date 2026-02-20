*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was easy. I made a list out of the countries, their codes, and flags. Then I iterated through the list to find the country based on their code, and returned the flag.***

****
## [2026 Winter Games Day 1: Opening Day](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-06)

Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding challenges inspired by them.

For the first one, you are given a two-letter country code and need to return the flag emoji for that country.

Use this list:

****
    1. get_flag("AL") should return "🇦🇱".
    2. get_flag("AD") should return "🇦🇩".
    3. get_flag("AR") should return "🇦🇷".
    4. get_flag("AM") should return "🇦🇲".
    5. get_flag("AU") should return "🇦🇺".
    6. get_flag("AT") should return "🇦🇹".
    7. get_flag("AZ") should return "🇦🇿".
    8. get_flag("BE") should return "🇧🇪".
    9. get_flag("BJ") should return "🇧🇯".
    10. get_flag("BO") should return "🇧🇴".
    11. get_flag("BA") should return "🇧🇦".
    12. get_flag("BR") should return "🇧🇷".
    13. get_flag("BG") should return "🇧🇬".
    14. get_flag("CA") should return "🇨🇦".
    15. get_flag("CL") should return "🇨🇱".
    16. get_flag("CN") should return "🇨🇳".
    17. get_flag("CO") should return "🇨🇴".
    18. get_flag("HR") should return "🇭🇷".
    19. get_flag("CY") should return "🇨🇾".
    20. get_flag("CZ") should return "🇨🇿".
    21. get_flag("DK") should return "🇩🇰".
    22. get_flag("EC") should return "🇪🇨".
    23. get_flag("ER") should return "🇪🇷".
    24. get_flag("EE") should return "🇪🇪".
    25. get_flag("FI") should return "🇫🇮".
    26. get_flag("FR") should return "🇫🇷".
    27. get_flag("GE") should return "🇬🇪".
    28. get_flag("DE") should return "🇩🇪".
    29. get_flag("GB") should return "🇬🇧".
    30. get_flag("GR") should return "🇬🇷".
    31. get_flag("GW") should return "🇬🇼".
    32. get_flag("HT") should return "🇭🇹".
    33. get_flag("HK") should return "🇭🇰".
    34. get_flag("HU") should return "🇭🇺".
    35. get_flag("IS") should return "🇮🇸".
    36. get_flag("IN") should return "🇮🇳".
    37. get_flag("IR") should return "🇮🇷".
    38. get_flag("IE") should return "🇮🇪".
    39. get_flag("IL") should return "🇮🇱".
    40. get_flag("IT") should return "🇮🇹".
    41. get_flag("JM") should return "🇯🇲".
    42. get_flag("JP") should return "🇯🇵".
    43. get_flag("KZ") should return "🇰🇿".
    44. get_flag("KE") should return "🇰🇪".
    45. get_flag("XK") should return "🇽🇰".
    46. get_flag("KG") should return "🇰🇬".
    47. get_flag("LV") should return "🇱🇻".
    48. get_flag("LB") should return "🇱🇧".
    49. get_flag("LI") should return "🇱🇮".
    50. get_flag("LT") should return "🇱🇹".
    51. get_flag("LU") should return "🇱🇺".
    52. get_flag("MG") should return "🇲🇬".
    53. get_flag("MY") should return "🇲🇾".
    54. get_flag("MT") should return "🇲🇹".
    55. get_flag("MX") should return "🇲🇽".
    56. get_flag("MD") should return "🇲🇩".
    57. get_flag("MC") should return "🇲🇨".
    58. get_flag("MN") should return "🇲🇳".
    59. get_flag("ME") should return "🇲🇪".
    60. get_flag("MA") should return "🇲🇦".
    61. get_flag("NL") should return "🇳🇱".
    62. get_flag("NZ") should return "🇳🇿".
    63. get_flag("NG") should return "🇳🇬".
    64. get_flag("MK") should return "🇲🇰".
    65. get_flag("NO") should return "🇳🇴".
    66. get_flag("PK") should return "🇵🇰".
    67. get_flag("PH") should return "🇵🇭".
    68. get_flag("PL") should return "🇵🇱".
    69. get_flag("PT") should return "🇵🇹".
    70. get_flag("PR") should return "🇵🇷".
    71. get_flag("RO") should return "🇷🇴".
    72. get_flag("SM") should return "🇸🇲".
    73. get_flag("SA") should return "🇸🇦".
    74. get_flag("RS") should return "🇷🇸".
    75. get_flag("SG") should return "🇸🇬".
    76. get_flag("SK") should return "🇸🇰".
    77. get_flag("SI") should return "🇸🇮".
    78. get_flag("ZA") should return "🇿🇦".
    79. get_flag("KR") should return "🇰🇷".
    80. get_flag("ES") should return "🇪🇸".
    81. get_flag("SE") should return "🇸🇪".
    82. get_flag("CH") should return "🇨🇭".
    83. get_flag("TH") should return "🇹🇭".
    84. get_flag("TT") should return "🇹🇹".
    85. get_flag("TR") should return "🇹🇷".
    86. get_flag("UA") should return "🇺🇦".
    87. get_flag("AE") should return "🇦🇪".
    88. get_flag("US") should return "🇺🇸".
    89. get_flag("UY") should return "🇺🇾".
    90. get_flag("UZ") should return "🇺🇿".
    91. get_flag("VE") should return "🇻🇪".
