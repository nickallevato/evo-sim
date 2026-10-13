# L2 quotes: verbatim source text for every number in `l2_inputs.json`

Run task EVO-43, search protocol of `research/checks/l2_hardness.py` (registration `ade0542`), access date 2026-10-13 for every item.
Fetched files live under the gitignored `sources/raw/l2-2026-10-13/<screen id>/`; the sha256 is of that raw file.
These quotes belong here, not in `docs/research/sources/quotes-literature.md`, because the analyst does not write the
shared quotes and bib files (agent rule); the operator copies the admitted rows across at integration.

Text extraction: PDFs with `pdftotext -layout` (poppler; parsed, not executed), XML with tags stripped. Quotes are copied
from that text layer as extracted, so line-break hyphens, OCR noise and table layout are kept. Where a table row was split
by the layout, the quote gives the labels and the value block separately, in source order. "OpenAlex abstract" means
the `abstract_inverted_index` of the OpenAlex record, put back together in position order (deterministic; punctuation
is part of the tokens). "EPMC abstract" means the raw `abstractText` field of the Europe PMC record.

Notation: Im = Crow's mortality component (Pd/Ps), If = Crow's fertility component (Vf/x^2), Ps = share surviving to
reproductive age. Values marked *derived* in `l2_inputs.json` use only the identities printed in the same source
(Im = Pd/Ps, Ps = 1 - Pd, I = Im + If/Ps).

## Route (b): admitted (pre-transition under the E2 operational rule, see `l2_screening.tsv` header)

### Salzano1979: C0211 (sha256 63b35accfa1ef1fe49f47f072b49996e9219f232177ce7a28b19afc05d4e50e7)
Salzano FM, Callegari-Jacques SM, Neel JV. 1979. Demografia genética dos índios Ticuna da Amazônia. Acta Amazonica 9(3):517-527. doi:10.1590/1809-43921979093517 (SciELO PDF).
> "Ticuna                         Presente comunicação                                  0,33               0,15           0.20                 0.54"
> - id: L2Q-01; locator: Tabela 9, last row; column heads "lm  If  lfj ps" and total (I); role: Im, If, If/Ps, I
> "Os Ticuna, que dependem bas- tante da pesca e da agricultura para a sua sub- sistência"
> - id: L2Q-02; locator: Discussão (p. 525 col. 1, layout-joined); role: E2, subsistence population
> "pela variância no número de crianças nas- cidas vivas em famíl ias completas (8,3). que é apenas um pouco maior do que a média (7,4) ."
> - id: L2Q-03; locator: Resultados, before Discussão; role: E2, mean completed live births 7.4; no contraception mentioned anywhere in the text (grep "anticoncep|controle": no hit)

### Goicoechea2000: C0848 (sha256 410de1778133ba45ce0f7746593f3603e66430102327902e526e897271e6bf2d)
Goicoechea AS, Carnese FR, Caratini AL, Avena SA, et al. 2000. Demography, genetic diversity, and population relationships among Argentinean Mapuche Indians. Genet Mol Biol 23(3):513-518. doi:10.1590/S1415-47572000000300001.
> "Opportunity for selection ***    Blancura Centro" / "Anecón Grande" / "Cerro Policía" / "Aguada Guzmán" ; value block: "Im             If                 If/ps                 I / 0.20           0.22                0.26                0.46 / 0.22           0.14                0.17                0.39 / 0.11           0.25                0.28                0.39 / 0.11           0.47                0.54                0.63"
> - id: L2Q-04; locator: Table II, panel "Opportunity for selection", rows in source order; role: Im, If, If/ps, I per community
> "The demographic and protein results for Blancura Centro were taken from Carnese et al. (1996)."
> - id: L2Q-05; locator: Material and Methods; role: Blancura Centro row is a relay, not admitted (rule 2)
> "Fertility was high in three of the four populations (about 7-8 children per mother who completed reproduc-"
> - id: L2Q-06; locator: Results para. 2; role: E2. Table II completed families: Anecón Grande "7.8 ± 0.8", Cerro Policía "7.0 ± 0.8", Aguada Guzmán "3.8 ± 0.4"
> "The low number of children per completed family in Aguada Guzmán suggests or indicates that non-Indian fertility control measures are presently be- ing taken in this community"
> - id: L2Q-07; locator: Discussion; role: E2 fails for Aguada Guzmán

### Nowak2013: C0821 (sha256 3eb8897051f13e4d04d21630d9b60f79eae34559ab02bf642ae90c6508acd0b1)
Nowak O, Liczbińska G, Piontek J. 2013. Opportunity for the operation of natural selection in a contemporary local population (the case of Slovincians). Advances in Anthropology 3(3):121-126. doi:10.4236/aa.2013.33016.
> "Generation                 N             x            SD             Pd     Ps         Vf          x2          Im          If          I / 1st generation             32           6.75          2.78          0.31    0.66        7.93      62.88        0.46       0.17        0.63 / 2nd generation              116          6.02          2.82          0.17    0.82        7.74      59.90        0.21       0.22        0.43"
> - id: L2Q-08; locator: Table 1; role: Pd, Ps, Im, If per generation. Note: printed Ps 0.66 differs from 1 - Pd = 0.69, and the printed I equals Im + If (this source's formula line reads "I = I m + If"); the registered mapping uses the printed Im, If and Ps
> "calculated for both generations: that born up to 1900 and at the beginning of the 20th century"
> - id: L2Q-09; locator: Results and Discussion para. 1; role: period
> "Although both generations had some knowledge of birth con- trol methods and agents, they did not use them consciously nor planned the number of children in a family in advance."
> - id: L2Q-10; locator: Results and Discussion; role: E2 (natural fertility, both generations)

### Posukh1990: C0710, EPMC abstract, PMID 2079207 (search file `search/epmc_Qb3.json`, sha256 68b50df24e62f037eb5f12caec79fa7ef632c76f79845a891af108ea591ee6a2)
Posukh OL, Vibe VP, Sukernik RI. 1990. [Genetic and ecologic study of aboriginal inhabitants of the Siberian northeast. III. Demographic structure of three modern population links of Yakutia]. Genetika 26:1628-1636. Full text closed; abstract only.
> "The mean and variance of livebirths per female, whose reproduction was completed, were 7.23 and 13.07, respectively."
> - id: L2Q-11; locator: EPMC abstract; role: E2 (mean completed live births 7.23)
> "The Crow's index of the opportunity for selection (It) and its components (Im and If) were found to be 0.62, 0.30 and 0.25, respectively."
> - id: L2Q-12; locator: EPMC abstract; role: Im, If (Evens, three populations pooled)

### Posukh1996: C0705, EPMC abstract, PMID 8964469 (same search file and sha256 as Posukh1990)
Posukh OL, Osipova LP, Kriukov IuA, Ivakin EA. 1996. [Genetic-demographic analysis of the population of native inhabitants of the Samburg tundra]. Genetika 32:822-829. Full text closed; abstract only.
> "It is demonstrated that the average number and variance of births for Tundra Nentsi women who have passed their reproductive years are 7.55 and 11.07, respectively. Crow's index of total selection (Itot) and its components (Im, I(f)) were 0.75, 0.47, and 0.19, respectively."
> - id: L2Q-13; locator: EPMC abstract; role: E2 (7.55) and Im, If

### Albeza2002: C0212 (sha256 45839d5c4ad99733937e1093876979bc2ef4eb4451537e58a2f4f8e57efeeedd)
Albeza MV, Acreche NE, Caruso GB. 2002. Biodemografía en poblaciones de la Puna (Chañarcito, Santa Rosa de los Pastos Grandes y Olacapato) Salta, Argentina. Chungara 34(1). doi:10.4067/S0717-73562002000100007.
> "Índice de Oportunidad para la Selección               0,44                         0,43                             0,30 / Componente de Mortalidad                              0,13                         0,09                             0,10 / Componente de Fecundidad                              0,28                         0,32                             0,19"
> - id: L2Q-14; locator: Tabla 1, columns Chañarcito, Santa Rosa de los Pastos Grandes, Olacapato; role: I, Im, If
> "If / ps para Chañarcito es de 0,32, representando el 72,23 % del Índice total; para Santa Rosa es de 0,35, el 80,64% y para Olacapato es de 0,20, el 65,57%"
> - id: L2Q-15; locator: Resumen; role: confirms "Componente de Fecundidad" is If (If/ps printed separately)
> "Hijos Nacidos Vivos                         6,23           6,44           5,60          5,79           5,86         6,87"
> - id: L2Q-16; locator: Tabla 2, columns Varones/Mujeres per locality; role: E2 (women: Chañarcito 6.44, Santa Rosa 5.79, Olacapato 6.87; not stated to be completed families)

### Moorad2013: C0136 (NCBI efetch PMC3675805 XML, sha256 9c8da42df34f41845652081309adef9495271351754eeaddf8c51d8fd09304ce)
Moorad JA. 2013. A demographic transition altered the strength of selection for fitness and age-specific survival and fertility in a 19th century American population. Evolution 67(6):1622-1634. doi:10.1111/evo.12023.
> "Proportional contributions of age-specific survival to total selection (the complement to age-specific fertility) diminished from approximately 1/3 to 1/7 following a marked increase in infant survival."
> - id: L2Q-17; locator: Abstract; role: viability share, early cohorts ~1/3, late cohorts ~1/7 (approximate as printed; exact values are in figures only, E5)
> "The study system is a female population of humans born between 1830 and 1894 who lived in what is now the state of Utah in the western USA."
> - id: L2Q-18; locator: Introduction, last para.; role: population, period
> "I caused by survival variance in the first year of life, I p (1) , decreased by slightly more than half ( Fig. 8 )."
> - id: L2Q-19; locator: Results; role: E3 (survival from the first year of life enters the decomposition). Flag: the data set is "females known to have reproduced" weighted for nulliparity (Methods), and the survival share covers all ages, not only pre-reproductive ones

## Route (a): admitted

### MadsenRobertsonYe2019wp: C1440 (UWA repository PDF, sha256 c24bca98e1bc96aff0e6ab5c7ee42c882e1c1c509aa38fb5648e9b8e3cdd3903)
Madsen JB, Robertson PE, Ye L. 2019. Malthus was right: explaining a millennium of stagnation. UWA Discussion Paper DP19.16 (working-paper version of Eur Econ Rev 2019, doi:10.1016/j.euroecorev.2019.05.004, which is C1433; the published text was not fetched; numbers may differ from it).
> "We therefore include country and time fixed effects in the models and use the SUR estimator, and find evidence of strong population convergence. Specifically, we find γ̂ = −0.028 over the full period (column 2), which implies much faster convergence, with a half-life of 11 years."
> - id: L2Q-20; locator: section on population convergence, text after "Table 3 reports the results of estimating equation (12)"; role: preferred specification and half-life
> "ln Lit−T −0.002 −0.028 −0.034 −0.032 −0.029 −0.029 −0.021*** (0.0001) (0.0006) (0.0004) (0.0006) (0.0003) (0.0004) (0.0006)"
> - id: L2Q-21; locator: Table 3 "Population Convergence (Eq.12)", row ln L(t-T), columns (1)-(7); role: gamma and robust SE (column 2: -0.028, SE 0.0006)
> "This implies a half-life of h = 336 years, where h = − ln(2) /(ln(1 + γ̂T )/T ). Again, the coefficient of initial population is likely to be biased towards zero"
> - id: L2Q-22; locator: same paragraph; role: the source's half-life formula (used to map gamma +- 1.96 SE to T), and the authors' reason for not preferring OLS column (1)
> "Est. period 1470-1870 1470-1870 1470-1600 1600-1870 930-1870 930-1870 930-1870" ; "Est. interval 30-yr 30-yr 30-yr 30-yr 30-yr 30-yr 30-yr" ; "The 9-country sample consists of: Austria, Belgium, France, Germany, Italy, the Netherlands, Spain, Sweden, and the UK."
> - id: L2Q-23; locator: Table 3 rows and notes; role: period (pre-transition, E2), regressor is log population (E3), 30-year interval

## Route (b): entered with E2 = false (modern or unclear; they enter only the registered "modern included" sensitivity line)

| id | screen id, bib id | sha256 (file) | quote (verbatim) | locator |
|---|---|---|---|---|
| L2Q-24 | C0126 Sohkhlet2013 | 24ed3dd1f412f864bae22a4e43c2e50b27ed852b94d914669f4522d441193b49 | "It was found that the value of I , I f and I m , calculated according to Crow's formula (1958),[ 6 ] was 0.4795, 0.2660 and 0.1687, respectively." ; "better living condition and health-care system among the Gowdas" ; "The mean number of live births to such mothers was found to be 3.0439" | Results; Abstract; Results |
| L2Q-25 | C0692 Gautam2009 | 901fb913aa0019883226138ff4324e02ec1cf52356d4f6daa30c8195a286f2b8 | "Kinnaura (Pooled) 0.163 0.837 0.194 0.159 0.384 49.48 50.52" (columns "P d P a s I m I f I t", % fertility, % mortality) | Table 3 |
| L2Q-26 | C0208 Adak2023 | 8bd3f8ccfe0346f702abe4b68bd0f2a1211e95c012376702b2063dd95f6c92d3 | "Differential fertility is 0.3134 and differential mortality is 0.1393, whereas, index of total selection intensity is 0.4964 according to Crow’s (1958) formula" ; population "living in a peri-urban setting" | Abstract |
| L2Q-27 | C0835 Bajpai2016 | 620ad10cf496421f19a222c34e19f8694a8591a6ecd44788bad1c9640a709423 | "Proportion of surviving (Ps)          0.9846         0.9538        0.9842        0.9844" ; "Index of mortality Im = Pd /Ps        0.0152         0.0483        0.0159        0.0157" ; "Index of fertility If = Vf /X2        0.3450         0.4260        0.3636        0.3750" (columns Brahmin, Kshatriya, Vaishya, Shudra) | Table 1 |
| L2Q-28 | C0796 Dharani2003 | f89315bcf5e13daa7108ddb1d279161fac8eaf7167d3bd330c7a0bbc5dd93c26 | "Population         I                Im         If /Ps       % If /Ps" ; "U+R              0.4263          0.0987       0.3276         76.85" ; "awareness of family planning" | Table 3; text |
| L2Q-29 | C0836 Elchinova2023 | 2f97fe6df7fc1557828c8d66cd36f6a84bc04a963f767339bbfef5d9f4954c4f | "Индекс Кроу [8] составил: ... Im = 0.004, If = 0.110, Itot = 0.115" (layout-interleaved with a table; the ellipsis marks interleaved table cells) ; prenatal losses "включая медаборты" | Results |
| L2Q-30 | C0825 Bharathi2019 | 4d9975a9e916a8724cdd4dcd2d9834b7fad47df7308044bad17e0bb552deba79 | "The mortality (Im) component was found to be 0.2151 while fertility (I f) component was found to be 0.1712." ; "the average live births per mother (X) ... of 40 years and above is 4.04" | Abstract; Results |
| L2Q-31 | C0841 Garh2022 | ced6887119cc3d3c33f9610ebc3062e76fb5e2e2edbceca0576b384e4ec38680 | "Crow (1958) Im 0.0377 If 0.1079 I 0.1497" ; "The average number of live birth per mother is 2.62±0.10" | Table 2; text |
| L2Q-32 | C0823 Saheb1982 | 1f530d5f2b9ee4ad22eb3f575b7f6f17a3e67fc647dbafdf3eaf840dbf56be87 | "The number of liveborn children per mother aged 40 and over is found to be 4.54, with variance of 4.93. In terms of frequency the, subadult mortality is 8.00%/o.Therefore the fertility component of Crow's index is 0.24 whereas the mortality component is 0.09." | Results (OCR text layer) |
| L2Q-33 | C0827 Saheb1983 | c695b3adde4768907cca2fec7eefbcbd1d212eba599e82ce863fdb3821ec103e | "The fertility component of the Crow's index is 0.25, whereas the mortality component is 0.06." ; summary: "Populacja ta znajduje s:ię w przejściowej fazie" | Results (OCR); Polish summary |
| L2Q-34 | C0780 Berdychowski1978 | 601c63dd022f082fd2705f59d3e79e45e22ba0d98d6ccb3e4af09e17e88a9749 | "Ludność badana | 0,110| 0,252| 0,361| dane własne" (columns Im, If, I) | Tab. 2 (OCR) |
| L2Q-35 | C0848 Goicoechea2000 | as L2Q-04 | Aguada Guzmán row of L2Q-04 with L2Q-07 | Table II |
| L2Q-36 | C0212 Albeza2002 | as L2Q-14 | Santa Rosa column of L2Q-14 with L2Q-16 (women 5.79) | Tabla 1, Tabla 2 |
| L2Q-37 | C0136 Moorad2013 | as L2Q-17 | late cohorts "1/7" of L2Q-17 | Abstract |
| L2Q-38 | C0746 Krishnan2000, OpenAlex abstract W2771031707 (`search/oa_Qb3.json`, sha256 8acb6f83967096df0f1dbe0a83c56630e332309b0d5ab3a1c975280f6dd2dfdc) | 8acb6f83... | "The average number of live birth is noticed to be 5.26 with variance 8.11. The mortality component Im is 0.2195 and the fertility component is If is 0.2931." | OpenAlex abstract |
| L2Q-39 | C0761 Little2006, OpenAlex W2132403081 (same file) | 8acb6f83... | "resulting in a marked decrease in the mortality component (Im) of selection (0.626 and 0.019, respectively) and total opportunity for selection (I = 1.312 and 0.272, respectively)." (1978 and 2000; If derived as (I - Im) x Ps, Ps = 1/(1 + Im)) | OpenAlex abstract |
| L2Q-40 | C0779 Dinsmore1985, OpenAlex W2460113205 (same file) | 8acb6f83... | "Crow’s index reflects these decreases, as the fertility component was 0.324 in 1850 and 0.308 in 1900. The mortality component was 0.318 in 1850 and 0.225 in 1900." | OpenAlex abstract |
| L2Q-41 | C0798 Kumar2015, OpenAlex W2260508941 (same file) | 8acb6f83... | "The index of selection due to fertility (If) was found to be 0.158, which is less than the index of mortality (Im = 0.201)" | OpenAlex abstract |
| L2Q-42 | C0703 Osipova1997, EPMC PMID 9480220 (`search/epmc_Qb3.json`) | 68b50df2... | "the average number of surviving children and pregnancies per female was 4.9 and 5.3, respectively" ; "the differential fecundity component, I(f) = 0.40, whereas the prereproductive mortality component (Im = 0.16)" | EPMC abstract |
| L2Q-43 | C0700 Tarskaya2002, EPMC PMID 12174592 (same file) | 68b50df2... | "The mean number of children per woman constituted 4.605. Crow's index and its components (Im and If) were 0.483, 0.104, and 0.343, respectively." | EPMC abstract |
| L2Q-44 | C0764 Magalhaes1987, OpenAlex W1981633590 (`search/oa_Qb3.json`) | 8acb6f83... | "The contribution of prereproductive mortality (Im = 0.28) was 40% higher than that of fertility (If = 0.20)." | OpenAlex abstract |
| L2Q-45 | C0808 ChandraSekar1998, OpenAlex W2769619994 (same file) | 8acb6f83... | "Crow’s index of opportunity of Selection (I) is 0.336." ; "Mortality Component (Im) is (0.075)" ; "Koraga have a mean live births of 3.97." (If derived as (I - Im) x Ps) | OpenAlex abstract |
| L2Q-46 | C0806 Salzano1970, OpenAlex W2042223084 (same file) | 8acb6f83... | "high mortality (36% of them die before the age of reproduction), low fertility (average of 3.6 livebirths per female who completed her reproductive performance)" ; "The index of opportunity for selection (0.88)" (Pd = 0.36; Im, If derived) | OpenAlex abstract |
