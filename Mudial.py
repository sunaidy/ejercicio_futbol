#! /usr/bin/python
from Grupo import Grupo

primer_grupo=  Grupo(['Colombia', 'Japonas', 'Senegal', 'Polonia'])

primer_grupo.match('Senegal', 2, 'Colombia', 3);
primer_grupo.match('Japonas', 2, 'Polonia', 5);
primer_grupo.match('Senegal', 0, 'Japonas', 3);
primer_grupo.match('Polonia', 0, 'Colombia', 1);
primer_grupo.match('Polonia', 1, 'Senegal', 4);
primer_grupo.match('Colombia', 2, 'Japonas', 1);



primer_grupo.result()


grupo=  Grupo(['Colombia', 'Japonas', 'Senegal', 'Polonia'])

grupo.match('Senegal', 2, 'Colombia', 3);
grupo.match('Japonas', 5, 'Polonia', 5);
grupo.match('Senegal', 0, 'Japonas', 3);
grupo.match('Polonia', 2, 'Colombia', 1);
grupo.match('Polonia', 1, 'Senegal', 4);
grupo.match('Colombia', 2, 'Japonas', 1);

grupo.result()