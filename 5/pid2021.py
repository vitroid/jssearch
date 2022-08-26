import json
import sys

# 0823版に修正済み
data = """
71009	tfujishiro@mail.saitama-u.ac.jp	藤城　貴史	10007	3E-07
71010	n.maron2070@gmail.com	大谷　奈央	10022	PE1-001
71011	2316124@gmail.com	宗重　海斗	10028	2Fb-03
71013	m21J6003@kanto-gakuin.ac.jp	沖口　陸	10069	PF2-001
71014	m20J6002@kanto-gakuin.ac.jp	板倉誠	10071	PF2-002
71015	f18K3003@kanto-gakuin.ac.jp	阿部　真弓	10088	PF2-003
71016	yuma_morii@chem.eng.osaka-u.ac.jp	森井佑真	10090	PC1-001
71017	m214742@hiroshima-u.ac.jp	佐野　雄大	10018	PC1-002
71019	s-shimoyamay@g.ecc.u-tokyo.ac.jp	下山雄人	10119	PF2-004
71020	tsuge@sci.u-toyama.ac.jp	柘植　清志	10136	2Ab-04
71021	takezawa@chem.s.u-tokyo.ac.jp	竹澤 悠典	10145	PE1-002
71022	makoto@oec.chembio.nagoya-u.ac.jp	山下　誠	10146	2C-02
71023	masanori.wakizaka.a7@tohoku.ac.jp	脇坂　聖憲	10116	2Fa-15
71024	takumi_matsuzaki@chem.eng.osaka-u.ac.jp	松﨑　拓実 	10101	PA1-001
71025	15864717971@163.com	Yuhan Liu	10161	3Ab-01
71026	weng-zhewei@g.ecc.u-tokyo.ac.jp	翁 哲偉	10095	3Fb-03
71027	yuuka_kiyokawa@chem.eng.osaka-u.ac.jp	清川　結加	10089	PA1-035
71028	sak_kawakami@cc.nara-wu.ac.jp	川上果歩	10154	4Fb-06
71029	uaa_tsuruta@cc.nara-wu.ac.jp	鶴田　彩	10155	4Fb-05
71030	umehara-yoshihiko@g.ecc.u-tokyo.ac.jp	梅原　慶彦	10067	PD1-001
71031	arima.rena.932@s.kyushu-u.ac.jp	有馬怜那	10176	PF2-005
71032	cmm11120@ict.nitech.ac.jp	花田 剛	10093	PF1-019
71033	1321501@ed.tus.ac.jp	青木　航平	10204	PF2-006
71034	yoshida.n.ai@m.titech.ac.jp	吉田希生	10064	PF1-011
71035	1321586@ed.tus.ac.jp	中島涼	10203	PF2-007
71036	1320519@ed.tus.ac.jp	海野 竜馬	10209	PA1-067
71037	c_akatsuka@chem.eng.osaka-u.ac.jp	赤塚千春	10030	PA1-057
71038	kanako_okuda@chem.eng.osaka-u.ac.jp	奥田 佳那子	10215	PA1-052
71039	tamaki@organomet.chem.es.osaka-u.ac.jp	玉木 颯太	10010	4C-02
71040	1320609@ed.tus.ac.jp	持田隆成	10223	PA1-053
71041	taito_watanabe@chem.eng.osaka-u.ac.jp	渡部　太登	10195	2C-12
71042	zou.q.aa@m.titech.ac.jp	Quan ZOU	10065	PF2-008
71043	yoshidaa19@chem.sci.osaka-u.ac.jp	吉田　歩未	10120	4E-06
71044	kasai.ryota.16@shizuoka.ac.jp	嵩井陵太	10025	3Ab-05
71045	yr786286@cii.shizuoka.ac.jp	飯田　拓己	10183	PA1-054
71046	naotoach@gmail.com	小澤　尚斗	10041	PA1-058
71047	ishigaki.shuto.17@shizuoka.ac.jp	石垣秋斗	10113	PA1-059
71048	y-koga@fukuoka-u.ac.jp	古賀　裕二	10234	PA1-002
71049	m20sb024@vt.osaka-cu.ac.jp	野村 夏生	10197	PF2-009
71050	s17a6076km@s.chibakoudai.jp	鴇田夏輝	10236	PA1-013
71051	takuya_akai@chem.eng.osaka-u.ac.jp	赤井 拓哉	10249	PC1-003
71052	m20sb008@yj.osaka-cu.ac.jp	大島　健太	10199	PF1-041
71053	4274396177@edu.k.u-tokyo.ac.jp	Siyuan, YE	10181	PF1-029
71054	asami-mizuki361@g.ecc.u-tokyo.ac.jp	浅見美月	10258	PF1-030
71055	yonemura@kochi-u.ac.jp	米村俊昭	10276	PA1-003
71056	k_saito@chem.eng.osaka-u.ac.jp	斉藤加奈子	10277	2C-03
71057	daisuke_saito@eis.hokudai.ac.jp	齋藤大将	10188	PA1-004
71058	shinki_fujisawa@chem.eng.osaka-u.ac.jp	藤澤 信樹	10210	4C-01
71059	minamo@auecc.aichi-edu.ac.jp	稲毛正彦	10024	PC1-004
71060	zhouwei110875@g.ecc.u-tokyo.ac.jp	Zhou Wei	10061	3Fb-02
71061	antoku.n.aa@m.titech.ac.jp	安徳七海	10281	PA1-060
71062	t_kobayashi@chem.eng.osaka-u.ac.jp	小林利通	10283	PC1-005
71064	kioka-kaoru673@g.ecc.u-tokyo.ac.jp	Kaoru Kioka	10286	PF1-031
71065	sawayama114@g.ecc.u-tokyo.ac.jp	澤山　拓	10039	2Fa-09
71066	6824025761@edu.k.u-tokyo.ac.jp	武富大空	10190	PF1-032
71067	ikenoue.ocu@gmail.com	池上裕太	10238	PA2-043
71068	nozomi_yamaguchi@chem.eng.osaka-u.ac.jp	山口希海	10291	PF2-010
71069	hayato_tatewaki@chem.eng.osaka-u.ac.jp	帯刀　隼人	10301	PC1-006
71070	yusuke_nakayama@chem.eng.osaka-u.ac.jp	中山 雄介	10200	3C-03
71071	rk21f001@stkt.u-hyogo.ac.jp	池田　貴志	10273	2Fa-14
71072	misa_tomoda@chem.eng.osaka-u.ac.jp	友田　美紗	10252	PF1-012
71073	yamada.yasuyuki@h.mbox.nagoya-u.ac.jp	山田泰之	10322	2C-08
71074	pritamchemistry1994@gmail.com	Sadhukhan Pritam	10320	2Fa-11
71075	cyjg1701@mail4.doshisha.ac.jp	畑 真知	10211	4E-05
71076	ctwg0756@mail4.doshisha.ac.jp	上野　ジン	10257	PE1-003
71077	wv-calm2527@g.ecc.u-tokyo.ac.jp	水谷 凪	10074	PF1-033
71078	kentaro.kadota0601@gmail.com	Kentaro Kadota	10131	2Ab-08
71079	kobayashis19@chem.sci.osaka-u.ac.jp	小林翠穂	10338	3D-02
71080	1320618@ed.tus.ac.jp	吉田 悠人	10224	2Fa-05
71081	akada.y.aa@m.titech.ac.jp	赤田　雄治	10342	PB2-015
71082	pmy45120@s.okayama-u.ac.jp	髙原　一真	10012	PB2-014
71083	s2120349@s.tsukuba.ac.jp	長島 俊太郎	10026	PB1-001
71084	s2070007@ipc.fukushima-u.ac.jp	大内　壮人	10015	PA1-034
71085	maho_imai@chem.eng.osaka-u.ac.jp	今井 真秀	10096	PA1-030
71086	s2120313@s.tsukuba.ac.jp	赤木　慎太郎	10285	PA1-020
71087	minesato@iis.u-tokyo.ac.jp	中川　峰里	10189	PD1-002
71088	pedroprosa@cse.hokudai.ac.jp	Ferreira da Rosa Pedro Paulo	10360	4Fb-02
71089	m.kayanuma@aist.go.jp	栢沼　愛	10217	PC1-007
71090	fukui@res.titech.ac.jp	福井 智也	10343	2Aa-14
71091	kusunoseh17@chem.sci.osaka-u.ac.jp	楠瀬 ひなの 	10187	PD1-003
71092	tome.tamon.372@s.kyushu-u.ac.jp	當銘 多聞	10327	2Ab-07
71093	miwa.yusuke@g.mbox.nagoya-u.ac.jp	三輪　祐介	10336	PC1-008
71094	leouay.benjamin@chem.kyushu-univ.jp	LE OUAY Benjamin	10005	4Aa-05
71095	2637922665@g.ecc.u-tokyo.ac.jp	大江　功能	10043	PF1-034
71096	ando@soc.chem.es.osaka-u.ac.jp	安藤直輝	10375	PD1-004
71097	harada@soc.chem.es.osaka-u.ac.jp	原田　裕一	10374	PF1-020
71098	nishiz@rirc.osaka-u.ac.jp	西澤　颯人	10059	PA1-014
71099	20626013@edu.cc.saga-u.ac.jp	杉山　純也	10082	PA2-044
71100	20626006@edu.cc.saga-u.ac.jp	鐘ヶ江　郁弥	10084	PA1-021
71101	kitagawa@cheng.es.osaka-u.ac.jp	北河 康隆	10198	PB1-002
71102	joe.komeda@gmail.com	米田丈	10310	3Aa-04
71103	kato.m.bd@m.titech.ac.jp	嘉藤　幹也	10341	PA1-036
71104	miyazawa.keishi.113@s.kyushu-u.ac.jp	宮澤　圭史	10335	4E-03
71105	kamitakahara.kazuki.220@s.kyushu-u.ac.jp	上高原　一輝	10334	2Ab-06
71106	nakanank20@chem.sci.osaka-u.ac.jp	中南慧士	10226	PE1-004
71107	miura-takumi786@g.ecc.u-tokyo.ac.jp	三浦 匠	10050	PF1-035
71108	k_kawaji@c.s.osakafu-u.ac.jp	川地 奏	10393	2D-06
71109	nobuto@chem.sci.osaka-u.ac.jp	吉成　信人	10396	4Aa-01
71110	tanifuji@scl.kyoto-u.ac.jp	谷藤 一樹	10117	4E-02
71111	r-hariki@bfc.mls.eng.osaka-u.ac.jp	播木亮太朗	10292	2C-07
71112	s20d552@stu.kagawa-u.ac.jp	西村学章	10205	PB1-003
71113	yokoken4513@gmail.com	横井健汰	10173	2Fb-01
71114	s-naoki3117@g.ecc.u-tokyo.ac.jp	真田直樹	10218	PF1-036
71115	d191618@hiroshima-u.ac.jp	Ndaru Candra Sukmana	10397	4Aa-06
71117	t_ozawa@c.s.osakafu-u.ac.jp	小澤 智大	10401	3D-01
71119	shaoweiwayde@gmail.com	Shao-Wei Lo	10125	2Fa-13
71120	bb52121609@ms.nagasaki-u.ac.jp	小倉　祥太	10416	PA1-068
71121	h17s2048@gmail.com	山口涼雅	10413	4Ab-02
71122	tanaka.miho.858@s.kyushu-u.ac.jp	田中　美帆	10135	PE1-005
71123	1321527@ed.tus.ac.jp	金田龍之介	10419	PA1-037
71124	h20ms214@hirosaki-u.ac.jp	畑中 励介	10420	PA1-005
71125	naoka.amamizu@cheng.es.osaka-u.ac.jp	Naoka Amamizu	10130	PF1-013
71126	takashim@konan-u.ac.jp	髙嶋　洋平	10412	2Fa-10
71127	hoshino@tohoku.ac.jp	星野 哲久	10108	2B-16
71128	a.machida@dmb.chem.tsukuba.ac.jp	町田 彩香	10371	3Ab-02
71129	i-d1kjl41-26@g.ecc.u-tokyo.ac.jp	松田 一輝	10235	PF2-029
71130	19rb001e@rikkyo.ac.jp	有馬 弘晃	10227	3C-06
71131	1172416511@edu.k.u-tokyo.ac.jp	飯塚 知也	10248	PF2-030
71132	koizumi-yoshihiro@g.ecc.u-tokyo.ac.jp	小泉 慶洋	10160	4Aa-07
71133	kuwamuran12@chem.sci.osaka-u.ac.jp	桑村　直人	10255	3Aa-06
71134	3b19702@ed.tus.ac.jp	上田 大貴	10429	4E-07
71135	sumida.r.aa@m.titech.ac.jp	角田 瑠輝	10169	2Fb-09
71136	keigo.hello.56@icloud.com	長奎吾	10159	PB1-004
71137	ri21c014@stkt.u-hyogo.ac.jp	下元直樹	10348	PF2-011
71138	bb52121612@ms.nagasaki-u.ac.jp	岸川　亮	10434	PF1-021
71139	bb52121613@ms.nagasaki-u.ac.jp	木下佳奈	10435	PA1-038
71140	yabune@sci.osaka-cu.ac.jp	籔根夏希	10129	PA1-039
71141	subramaniam.jeevithra_dewi.sh9@ms.naist.jp	Jeevithra Dewi Subramaniam	10439	PA1-062
71142	ohtani@chem.kyushu-univ.jp	大谷亮	10445	2Fa-04
71145	shangxing_li@chem.eng.osaka-u.ac.jp	李 尚興	10047	PF1-022
71146	s213496m@st.yamagata-u.ac.jp	丸山 秀斗	10178	PF1-001
71147	wahyudiantob17@chem.sci.osaka-u.ac.jp	Benny Wahyudianto	10438	PC1-009
71148	nattaporu.ma.33a@st.kyoto-u.ac.jp	Nattapol Ma	10433	2Fa-12
71149	ctwf0772@mail4.doshisha.ac.jp	田中皐晴	10133	PE1-006
71150	s213942m@st.yamagata-u.ac.jp	寺島 僚	10246	PF1-002
71151	a17.b6ks@g.chuo-u.ac.jp	板垣 廉	10453	3C-05
71152	masada-koichiro210@g.ecc.u-tokyo.ac.jp	正田 浩一朗	10070	2D-14
71153	morozumi.n.aa@m.titech.ac.jp	Naoki MOROZUMI	10366	4Ab-01
71154	teraishi@organomet.chem.es.osaka-u.ac.jp	寺石　怜矢	10225	PD1-005
71155	21rmu06@ms.dendai.ac.jp	小管 亮太	10274	PD1-006
71156	y-shimoyama@aist.go.jp	下山　祥弘	10237	2C-06
71157	jito@oec.chembio.nagoya-u.ac.jp	伊藤　淳一	10157	PD1-007
71158	sc0075vi@ed.ritsumei.ac.jp	山口 健太	10027	4Fb-08
71159	hiromasa.sato@cheng.es.osaka-u.ac.jp	佐藤 宏賢	10457	PF1-023
71160	kojimat15@chem.sci.osaka-u.ac.jp	小島 達弘	10459	PA1-061
71162	ctwf0721@mail4.doshisha.ac.jp	川橋 桃瑛	10461	PE1-007
71163	yuuki-ino@g.ecc.u-tokyo.ac.jp	猪俣　祐貴	10299	3Aa-08
71164	gooz17@chem.sci.osaka-u.ac.jp	GOO Zi Lang	10446	3Ab-04
71165	alinduma18@gmail.com	Maulinda Kusumawardani	10422	PA1-063
71166	Matsumotoa19@chem.sci.osaka-u.ac.jp	松本　明	10444	PA1-040
71167	sc0088rx@ed.ritsumei.ac.jp	若狹　耀生	10029	PF1-014
71168	gr0451pe@ed.ritsumei.ac.jp	KUMAR Siddhant	10051	PA1-006
71169	sc0081hr@ed.ritsumei.ac.jp	椎名 麗	10045	PF1-015
71170	1321560@ed.tus.ac.jp	末安 啓悟	10406	PA1-045
71171	1321605@ed.tus.ac.jp	土方 岳哉	10405	PA1-015
71172	mc20017@shibaura-it.ac.jp	小林大巡	10239	PC1-010
71173	20lb013x@rikkyo.ac.jp	網野渚紗	10467	PC1-011
71174	mh1043@wakayama-u.ac.jp	平谷直也	10259	PC1-012
71175	mh1043@wakayama-u.ac.jp	山﨑　優	10263	PA1-064
71176	mh1043@wakayama-u.ac.jp	奥田　裕一	10262	PA1-065
71177	mh1043@wakayama-u.ac.jp	植田　悠斗	10261	PA1-055
71178	takeyama.t.ab@m.titech.ac.jp	竹山　知志	10242	3B-01
71179	m21sb028@ab.osaka-cu.ac.jp	前田　智也	10462	PA1-056
71180	m20sb023@vt.osaka-cu.ac.jp	西野　遼太郎	10122	PC1-013
71181	ms20821@st.kitasato-u.ac.jp	田中　鈴	10011	PC1-014
71182	t201a014@gunma-u.ac.jp	石関 遼介	10350	PD1-008
71183	fujii.ikuya.53m@st.kyoto-u.ac.jp	藤井 郁哉	10087	3D-04
71184	hayashi-yuki305@g.ecc.u-tokyo.ac.jp	林 柚希	10068	2Fa-08
71185	hino@chem.s.u-tokyo.ac.jp	日野　綾子	10311	PA1-041
71186	bb52120646@ms.nagasaki-u.ac.jp	楊益鳴	10436	PA1-042
71187	tnakazono@rikkyo.ac.jp	Takashi Nakazono	10303	3C-07
71188	ri20t018@stkt.u-hyogo.ac.jp	竹崎　駿	10414	4Ab-04
71189	20lb007t@rikkyo.ac.jp	関根　直輝	10150	PA1-043
71190	ryo-tab-j1311@g.ecc.u-tokyo.ac.jp	田淵 凌輔	10245	2Fb-10
71191	chi6para.omicron@gmail.com	大野　智世	10479	PA1-007
71192	s2120206@s.tsukuba.ac.jp	伊藤 帆奈美	115229	2Aa-13
71193	vai_aratani@cc.nara-wu.ac.jp	荒谷郁実	10278	PA1-022
71194	xu.wenhuang.378@s.kyushu-u.ac.jp	徐文煌 	10493	2B-15
71195	kukddx@gmail.com	関根 大修	10230	PD1-009
71196	1320514@ed.tus.ac.jp	伊藤寛朗	10282	PB2-013
71197	d0871004@edu.kit.ac.jp	藤井 俊樹	10424	PB2-012
71198	seki.rin.75r@st.kyoto-u.ac.jp	関　凜	10192	PD1-010
71200	nishi.masato.nk6@ms.naist.jp	西 正人	10408	PA1-016
71201	yuanfei-liu@chem.s.u-tokyo.ac.jp	Liu Yuanfei	10458	2Ab-16
71202	ryo.z84.carp@gmail.com	金子凌	115212	2B-04
71203	chengjiamin@mail.cstm.kyushu-u.ac.jp	Cheng Jiamin	2200929000	2C-05
71204	mh1043@wakayama-u.ac.jp	安上　昂輝	10264	PA1-066
71205	tatiana.gridneva1@oist.jp	Tatiana Gridneva	10428	PA1-017
71206	32411021@stn.nitech.ac.jp	臼井 彩希	10221	PD1-011
71207	i.daiki@dmb.chem.tsukuba.ac.jp	伊藤　大輝	10394	PA2-050
71208	baba31@rirc.osaka-u.ac.jp	馬場一彰	10509	PA2-045
71209	m20sb021@wy.osaka-cu.ac.jp	中西 真祐	10307	PA1-008
71210	ikeda@ms.ifoc.kyushu-u.ac.jp	池田　京	10118	PF1-024
71211	k.shima@cse.hokudai.ac.jp	島かおり	10092	4Fb-01
71212	cmm11030@ict.nitech.ac.jp	小川 和真	10506	PD1-012
71213	ikv12392@kwansei.ac.jp	稲石 陽斗	10241	2Aa-08
71214	songyu.spark@ees.hokudai.ac.jp	YU SONG	10316	2Fb-06
71215	s1891022@s.konan-u.ac.jp	田中進太郎	10471	PA1-069
71216	k.sagara@dmb.chem.tsukuba.ac.jp	相良　圭吾	10516	PA2-055
71217	pj.kou@imr.tohoku.ac.jp	Po-Jung Huang	10502	2Fa-16
71218	m216429@hiroshima-u.ac.jp	澁江 拓哉	10372	PC1-015
71219	20lb016s@rikkyo.ac.jp	藤野直人	114952	PC2-001
71220	sano-hiroyuki807@g.ecc.u-tokyo.ac.jp	佐野　鴻之	10491	2Fa-07
71221	hina_kashima@chem.eng.osaka-u.ac.jp	鹿島 日菜	10409	PC1-016
71222	m213446@hiroshima-u.ac.jp	黒目　武志	10518	4C-07
71223	s213299m@st.yamagata-u.ac.jp	安齋将	10517	PF1-016
71224	tanabe.tappei.q2@dc.tohoku.ac.jp	田邉辰平	10452	PB1-005
71225	s2120223@s.tsukuba.ac.jp	島村知成	10431	3Ab-03
71226	tateishi.tomoki.6e@kyoto-u.ac.jp	立石 友紀	10212	2Fb-13
71228	firereaction.soccer0307@gmail.com	五十嵐樹	10477	4C-04
71229	sakai.yuta@h.mbox.nagoya-u.ac.jp	坂井　優太	10073	4E-01
71230	r_yamashita@chem.eng.osaka-u.ac.jp	山下　廉	10344	PE1-008
71235	zhu.bo.6z@kyoto-u.ac.jp	ZHU Bo	10368	2D-04
71236	mengyinghan@chem.s.u-tokyo.ac.jp	HAN Mengying	10206	PF1-025
71237	inoue.i.ab@m.titech.ac.jp	井上 伊織	10085	4Aa-04
71238	teikin@ees.hokudai.ac.jp	XIN ZHENG	10216	2Fb-05
71244	akiyama-daichi674@g.ecc.u-tokyo.ac.jp	Daichi Akiyama	10399	PF1-026
71245	bb52320203@ms.nagasaki-u.ac.jp	山田　基貴	10367	PA2-033
71250	c.murata@ees.hokudai.ac.jp	村田　千夏	10103	PA2-056
71251	endo.kenichi.5m@kyoto-u.ac.jp	遠藤 健一	10541	3Fb-07
71252	a18.3wkw@g.chuo-u.ac.jp	宮川 竜一	10505	PC2-002
71253	fate.ty.bsb6@docomo.ne.jp	米永達哉	10547	PA1-009
71254	onozuka0514ryo@g.ecc.u-tokyo.ac.jp	小野塚 凌	10270	PA2-051
71255	rika.nakamura.r2@dc.tohoku.ac.jp	中村 理香	10492	PA1-018
71256	ri21v020@stkt.u-hyogo.ac.jp	中内 健司	10550	PA2-013
71257	shinya.takaishi.d8@tohoku.ac.jp	高石慎也	10468	2Fa-01
71258	t211a012@gunma-u.ac.jp	井ノ口　大翔	10503	PA1-010
71259	kikukawa@se.kanazawa-u.ac.jp	菊川雄司	10352	3Ab-06
71260	a4524053@edu.gifu-u.ac.jp	長谷川遥	10515	3Fb-01
71261	2461451185@edu.k.u-tokyo.ac.jp	Xiyuan Zhang	10137	2Fa-06
71262	f20a047f@mail.cc.niigata-u.ac.jp	渡邉真子	10182	PA1-011
71264	m0673015@edu.kit.ac.jp	隅田 滉史	10540	PA1-031
71265	h21ms207@hirosaki-u.ac.jp	齊藤　慧一郎	10562	PC2-003
71266	sudo0812@stu.kanazawa-u.ac.jp	須藤 涼	10561	2Fb-11
71267	r1zo1458@gmail.com	小久保　佳亮	10358	2Ab-05
71268	zhanghanci@g.ecc.u-tokyo.ac.jp	張 晗辞	10387	PE2-001
71273	g2040628@edu.cc.ocha.ac.jp	皆川佳央	10545	PF1-037
71280	ryu9712@stu.kanazawa-u.ac.jp	半田 龍之介	10196	PE1-009
71283	y-imai@apch.kindai.ac.jp	今井喜胤	10560	PF1-027
71284	k.shigehira@mail.cstm.kyushu-u.ac.jp	重平 健翔	10564	PA1-012
71285	ri20k028@stkt.u-hyogo.ac.jp	宮下花	10566	4Ab-07
71291	2033310140y@kindai.ac.jp	寺田　光太	10557	PA2-052
71292	6120023f@st.toho-u.jp	藤本 大地	10553	PA1-023
71293	silpa@chem.s.u-tokyo.ac.jp	Silpa Chandran Rajasree	10244	PE1-010
71294	taniguchi-akira793@g.ecc.u-tokyo.ac.jp	谷口　旺	10379	PF1-038
71295	a16.nmr7@g.chuo-u.ac.jp	鈴木　美香	10063	3D-03
71296	sunohara-haruka688@g.ecc.u-tokyo.ac.jp	春原晴香	10364	2Fb-14
71297	skasif@staff.kanazawa-u.ac.jp	Sk Asif Ikbal	10568	2Fb-12
71298	r202070120hh@jindai.jp	佐藤 由奈	10201	PF1-039
71299	k.ueno@mail.cstm.kyushu-u.ac.jp	植野 嵩大	10417	PF1-028
71301	1320503@ed.tus.ac.jp	新井　駿也	10171	PB1-006
71302	21lb013y@rikkyo.ac.jp	髙田里咲	10571	PC2-004
71303	z3921006@edu.gifu-u.ac.jp	高森敦志	10313	2Aa-16
71305	lemonade1653@eis.hokudai.ac.jp	安藤　廉平	10321	2D-13
71306	m20sb032@ty.osaka-cu.ac.jp	宮本 航輔	10532	PA2-001
71320	watanabe.h.bc@m.titech.ac.jp	渡邊　裕春	10269	PC2-005
71325	yoshiike-taiga@ed.tmu.ac.jp	吉池 大河	10049	3D-06
71327	sisnrinlo3ove@gmail.com	高橋　あすか	10040	2D-05
71328	akiyama.naoki.ag3@ms.naist.jp	秋山 直生	10214	PE2-002
71329	t-akiyama@organomet.chem.es.osaka-u.ac.jp	秋山 拓弥	10158	2D-11
71331	mhiro@kanagawa-u.ac.jp	廣津昌和	10525	PA1-044
71332	sumi1line@gmail.com	角谷 凌	10240	PF1-040
71335	n205213b@yokohama-cu.ac.jp	城田美月	10451	PF2-020
71337	koni524@cse.hokudai.ac.jp	小西　由姫	10143	PF2-021
71338	tomitay17@chem.sci.osaka-u.ac.jp	富田　悠介	10174	PE2-003
71339	1321537@ed.tus.ac.jp	玄番美都	10407	PA2-034
71340	t201a080@gunma-u.ac.jp	中村 亮太	10440	PA2-002
71341	a17.aanr@g.chuo-u.ac.jp	吉田 瑠佳	10574	PA2-046
71342	a16.n44f@g.chuo-u.ac.jp	澤口 玲実	10575	PE2-004
71343	bb52319201@ms.nagasaki-u.ac.jp	福元　良	10548	PF1-017
71344	okuyama-takahiro579@g.ecc.u-tokyo.ac.jp	奥山 貴太	10268	PA2-047
71345	ikemoto.satoru@b.mbox.nagoya-u.ac.jp	Satoru Ikemoto	10426	3Fb-08
71346	ohtsu@chem.titech.ac.jp	大津博義	10578	2B-08
71347	kasahara.nonoka.813@s.kyushu-u.ac.jp	笠原ののか	10579	PD1-013
71348	pei@chem.s.u-tokyo.ac.jp	XIAO-LI PEI	10271	2Ab-15
71349	yukitamura@kwansei.ac.jp	北村由羽	10478	PA1-070
71361	o.iwanaga.486@s.kyushu-u.ac.jp	岩永 修	10586	2Fb-08
71362	yuto.morimachi@gmail.com	森町 勇人	10546	PA1-032
71363	k-aoki-8bf@eagle.sophia.ac.jp	青木 香菜子	10345	PA2-003
71364	inaba.hiroaki@i.mbox.nagoya-u.ac.jp	稲葉大晃	10587	PF1-042
71365	matsu-9017@outlook.jp	松永恵也	10449	PF1-018
71366	tamon.yamauchi.q4@dc.tohoku.ac.jp	山内多聞	10585	PF2-012
71367	c5620037@aoyama.jp	田中 秀幸	10520	PB1-007
71368	chko16089@g.nihon-u.ac.jp	村田　浩平	10581	PA1-024
71369	1320508@ed.tus.ac.jp	石塚 友也	10588	PB1-008
71370	c5620041@aoyama.jp	町田 奏	10519	PB1-009
71371	isoroku@fukuoka-edu.ac.jp	長澤　五十六	10496	PB1-010
71372	1321552@ed.tus.ac.jp	佐藤 弘祐	115133	PA2-030
71373	a17.jkst@g.chuo-u.ac.jp	司馬　友里	10572	PC2-006
71374	t_misawa@sophia.ac.jp	三澤智世	10009	4Aa-02
71378	tmatsuo@ms.naist.jp	松尾　貴史	10166	2C-01
71380	s183197@stn.nagaokaut.ac.jp	大場 晶	10380	PA1-071
71381	a-yoneda@chem.eng.osaka-u.ac.jp	米田暁	10536	PA1-033
71382	HKominami@kwansei.ac.jp	小南 隼人	10485	3Fa-01
71384	m-sakaida@bfc.mls.eng.osaka-u.ac.jp	境田　萌	10295	2C-15
71385	s2120229@s.tsukuba.ac.jp	土岐恵莉佳	10600	PA1-025
71386	21lb008y@rikkyo.ac.jp	菅原大地	10272	2C-09
71387	takuto_109@icloud.com	徳永　拓人	10595	PE2-005
71388	ariyasu.shinya@j.mbox.nagoya-u.ac.jp	有安真也	10602	3E-06
71390	anliruisheng@gmail.com	安立 瑞生	10254	PB2-001
71391	yusuke.1998.12.19@gmail.com	堀田 佑介	10332	PB1-015
71392	1321623@ed.tus.ac.jp	宮嶋小百合	10331	PB2-002
71394	nozomi.tomioka@eagle.sophia.ac.jp	富岡 望	10275	PA2-031
71396	j.sekiguchi.742@ms.saitama-u.ac.jp	関口 珠恵理	10404	PD1-014
71397	n20m610@matsu.shimane-u.ac.jp	小原　吉浩	10608	PA2-014
71398	zhouzihan@mail.cstm.kyushu-u.ac.jp	周　子涵	10365	2C-13
71399	haruki.tanaka.t1@dc.tohoku.ac.jp	田中 陽樹	10463	PF1-003
71400	kawagoe@macro.t.u-tokyo.ac.jp	川越美花	10542	3D-07
71402	j.troyano.prieto@gmail.com	Javier Troyano	10613	3Fa-03
71403	2033320240b@kindai.ac.jp	松平　華奈	10421	PA1-026
71404	ntakeda@gunma-u.ac.jp	武田　亘弘	10584	PA2-004
71410	mukoyoshi@ssc.kuchem.kyoto-u.ac.jp	向吉　恵	10615	PA2-020
71412	ri20y026@stkt.u-hyogo.ac.jp	松田 雄貴	10220	PF2-040
71413	yoshino@chem.kyushu-univ.jp	芳野遼	10594	PF2-022
71414	katsuhirono00@eis.hokudai.ac.jp	大塚滉喜	10400	2C-11
71415	fan.zeyu.42c@st.kyoto-u.ac.jp	FAN Zeyu	10443	3Fa-08
71417	1810320699g@kindai.ac.jp	髙橋 直大	10056	PA1-027
71418	weishenglan1996@g.ecc.u-tokyo.ac.jp	Shenglan WEI	10552	2D-09
71419	t.yamasaki.840@ms.saitama-u.ac.jp	山崎　友実	10603	PA2-015
71420	hayakawa3743@g.ecc.u-tokyo.ac.jp	早川 覚博	10287	PA2-072
71421	j.yanagisawa@chem.kyushu-univ.jp	柳澤純一	10172	PA2-057
71423	uam_takubo@cc.nara-wu.ac.jp	田窪 瑞季	10423	3D-05
71424	xu.jianeng.487@s.kyushu-u.ac.jp	許 嘉能	10037	4Fa-01
71425	uay_fujisawa@cc.nara-wu.ac.jp	藤澤 良実	10425	2Ab-12
71427	miyaji.m.aa@m.titech.ac.jp	宮路雅彦	10086	PC2-007
71428	honda.megumi.047@s.kyushu-u.ac.jp	本多 めぐみ	10621	2Aa-15
71432	s.fujiwara.sphc@mail.cstm.kyushu-u.ac.jp	藤原才也	10589	2Fa-02
71437	h-yanase@chem.s.u-tokyo.ac.jp	梁瀬 大海	10253	PA1-073
71438	yu14121@eis.hokudai.ac.jp	久保田　悠斗	10624	PA2-035
71439	zhangzhi@mail.cstm.kyushu-u.ac.jp	ZHANG ZHI	10537	2C-14
71440	ikeda.s.aq@m.titech.ac.jp	池田 周平	10329	PA2-005
71441	tayier.fuerkaiti.77s@st.kyoto-u.ac.jp	FUERKAITI TAYIER	10411	PF2-031
71442	ctwf0740@mail4.doshisha.ac.jp	中原　寛樹	10300	4E-04
71444	ootake.kenichi.8a@kyoto-u.ac.jp	大竹 研一	10619	3Fa-02
71445	m.fujimoto.380@ms.saitama-u.ac.jp	藤本真由	10614	PA2-006
71446	tangpphuti@gmail.com	Phitchayapha Phattharaphuti	10442	2Ab-09
71450	nakada.773@g.chuo-u.ac.jp	中田明伸	10625	3Fb-04
71452	2033320237m@kindai.ac.jp	三嶋康平	10558	PA2-021
71453	y.ishida.404@ms.saitama-u.ac.jp	石田 優太	10632	PA2-036
71454	nishimura@soc.chem.es.osaka-u.ac.jp	西村 翔馬	10377	4Fb-07
71455	z4524003@edu.gifu-u.ac.jp	池田友哉	10628	PC2-008
71456	sd192004@cis.fukuoka-u.ac.jp	河野未来	10384	PA1-028
71457	akira-takahashi@aist.go.jp	Akira Takahashi	10611	3Fa-04
71459	miyak@ccs.tsukuba.ac.jp	宮川 晃一	10599	PB2-003
71460	haraguchi-naoya671@g.ecc.u-tokyo.ac.jp	原口直哉	10141	PF2-032
71465	kyamada@ees.hokudai.ac.jp	山田 和輝	10193	PA2-037
71466	iwai.yuudai.167@s.kyushu-u.ac.jp	岩井優大	10191	PB2-004
71467	mochinari0609@eis.hokudai.ac.jp	望月尊生	10376	PA2-067
71470	muramatsu.h.ae@m.titech.ac.jp	村松央教	10418	2Aa-12
71471	y_kagawa@chem.eng.osaka-u.ac.jp	香川 佳之	10637	3E-05
71472	ktakahashi@es.hokudai.ac.jp	高橋　仁徳	10508	2Fb-07
71474	s.yamada@kwansei.ac.jp	山田 咲樹	10480	2Aa-03
71481	y_yamauchi@chem.eng.osaka-u.ac.jp	山内泰宏	10144	2Ab-02
71482	core1800873@eis.hokudai.ac.jp	眞部 夢大	10513	2Ab-13
71486	sudaa@ees.hokudai.ac.jp	須田綾乃	10617	PD2-001
71489	m_abe@chem.eng.osaka-u.ac.jp	阿部　美笛	10256	PE2-006
71491	he@chem.s.u-tokyo.ac.jp	Wei He	10308	PF2-041
71495	beams_jackn@stu.kanazawa-u.ac.jp	日比 敏博	10500	2Fb-15
71496	t_hashimoto@chem.eng.osaka-u.ac.jp	橋本 大輝	10228	2D-12
71498	iitsuka.t.aa@m.titech.ac.jp	Tadatoshi Iitsuka	10472	PF2-013
71499	aoki.r.al@m.titech.ac.jp	青木 里紗	10523	PF2-042
71501	m_sakuraba@chem.eng.osaka-u.ac.jp	櫻羽　真煕	10081	PD2-002
71502	harada.yuuki@f.mbox.nagoya-u.ac.jp	原田 悠生	10083	2Fb-02
71503	tnakajima@chem.s.u-tokyo.ac.jp	中島朋紀	10641	3Aa-05
71504	y-yamada@chem.s.u-tokyo.ac.jp	山田 慶彦	10627	PA2-068
71506	shirai.sora@j.mbox.nagoya-u.ac.jp	白井 そら	10121	4Fb-04
71507	2033320222t@kindai.ac.jp	中井 大央	10325	PD2-003
71510	s-mafune0312@eagle.sophia.ac.jp	真船颯太	10629	PC2-009
71512	najuany@ees.hokudai.ac.jp	Najuan Yang	10315	PA2-069
71513	k.nakao.581@stn.nitech.ac.jp	仲尾健一	10473	2Ab-01
71517	shichino.masanori@g.mbox.nagoya-u.ac.jp	七野　正典	10153	PF2-014
71518	negita.kohei@k.mbox.nagoya-u.ac.jp	根喜田 康平	10177	PF2-033
71519	ytsubonouchi@eng.niigata-u.ac.jp	坪ノ内優太	10635	2C-10
71520	shinpei.kusaka@chembio.nagoya-u.ac.jp	日下心平	10648	2Aa-04
71521	dilip.pandey@oist.jp	Dilip Kumar Pandey	10460	2C-04
71522	bad.denchu.12@gmail.com	田中 沙樹	10306	PE2-007
71523	tokunaga.takaya@e.mbox.nagoya-u.ac.jp	德永 貴也	10098	2Fa-03
71524	nakagawa.misaki@a.mbox.nagoya-u.ac.jp	中川 岬	10112	PA2-058
71526	ctwg0736@mail4.doshisha.ac.jp	西川敦士	10633	PB2-005
71536	mitsumoto-taichi646@g.ecc.u-tokyo.ac.jp	光本 泰知	10383	2D-10
71543	sugiura.hikaru@e.mbox.nagoya-u.ac.jp	杉浦 光	10099	PF2-034
71545	kawamura.aya@g.mbox.nagoya-u.ac.jp	川村 彩	10134	PF2-035
71546	sugiyama.t.al@m.titech.ac.jp	杉山 傑	10647	PA2-007
71547	lazuly526chemi@icloud.com	渡邊佳乃子	10659	PA2-053
71549	shinozaki.k.ac@m.titech.ac.jp	篠崎　和樹	10521	PA2-038
71550	shira.chem@eis.hokudai.ac.jp	白倉 逸人	10267	PA2-059
71551	suginome@macro.t.u-tokyo.ac.jp	杉野目　駿	10148	3Fa-06
71552	m202154@hiroshima-u.ac.jp	高嶋賢太郎	10280	PC2-010
71553	aoyama.toi@i.mbox.nagoya-u.ac.jp	青山 冬威	10114	PA2-060
71554	okuran19@chem.sci.osaka-u.ac.jp	大倉 望生	10395	PA2-039
71557	tokuda.shun.38n@st.kyoto-u.ac.jp	徳田駿	10167	PD2-004
71558	hira@stu.kanazawa-u.ac.jp	平澤晃	10305	PA2-061
71559	scb02128@edu.osakafu-u.ac.jp	真下　理彩	10618	PF2-036
71561	micchi0232@ezweb.ne.jp	大城　実之	10638	2B-01
71562	kanno-t@chem.s.u-tokyo.ac.jp	Takefumi Kanno	10456	2Aa-02
71565	a11.bdsw@g.chuo-u.ac.jp, chang@kc.chuo-u.ac.jp	山田　将大	10576	4C-03
71566	ishizaki.toshiharu@nihon-u.ac.jp	石崎 聡晴	10229	PA2-022
71567	hiwatashi@imr.tohoku.ac.jp	樋渡 淑恵	10288	4Fa-06
71569	sugawa.t.aa@m.titech.ac.jp	Tsuyoshi Sugawa	10109	4Aa-03
71570	207d1311@st.kumamoto-u.ac.jp	杉本 祥	10652	3Aa-02
71571	D20sb003@yf.osaka-cu.ac.jp	松谷 崇生	10640	PD2-005
71573	2033310110m@kindai.ac.jp	西山智貴	10382	PB2-006
71575	i2033013@edu.cc.uec.ac.jp	伊藤 沙紀	10650	2B-09
71576	m0671006@edu.kit.ac.jp	大石 圭悟	10008	4C-06
71577	kentaro_aoki@ssc.kuchem.kyoto-u.ac.jp	青木健太郎	10296	PA1-029
71578	moriyama.hayato.54m@ssc.kuchem.kyoto-u.ac.jp	森山 隼人	10356	2B-05
71580	hiroshi.sato@riken.jp	佐藤　弘志	10662	2Fb-16
71581	1321569@ed.tus.ac.jp	高塚　一穂	10663	PA2-040
71582	fujimoto@bfc.mls.eng.osaka-u.ac.jp	藤本　智広	10294	2C-16
71583	yulin@crec.t.u-tokyo.ac.jp	YULIN ZHANG	10362	2D-01
71584	wang.xiaoguang@i.mbox.nagoya-u.ac.jp	Xiaoguang Wang	10170	PA2-023
71585	sab02116@edu.osakafu-u.ac.jp	廣内 駿	10604	PF2-037
71586	futo.chem.fromkindai@gmail.com	小泉　風音	10622	PD2-006
71587	kuidichi@outlook.jp	加藤賢太	10672	PC2-011
71588	z4524011@edu.gifu-u.ac.jp	岩崎 太亮	10078	PA1-074
71589	kunal-k@chem.s.u-tokyo.ac.jp	KUNAL KUMAR	10370	4Fb-03
71590	z4524061@edu.gifu-u.ac.jp	長澤　樹	10512	PF1-004
71591	k_nakayama@eagle.sophia.ac.jp	中山 海斗	10643	PA2-041
71592	1321614@ed.tus.ac.jp	逸見　研士郎	10390	PD2-007
71593	olaf@chem.s.u-tokyo.ac.jp	Olaf Stefanczyk	10361	4Fa-04
71594	wang-jh@chem.s.u-tokyo.ac.jp	Junhao Wang	10354	4Fa-02
71595	fkobayashi@rs.tus.ac.jp	小林　文也	10656	4Fa-05
71596	wsuzuki@scl.kyoto-u.ac.jp	鈴木航	10645	PA2-008
71597	suzuki.t.ef@m.titech.ac.jp	鈴木　輝哉	10680	PD2-008
71598	1320575@ed.tus.ac.jp	棚橋 耕太郎	10389	PF2-015
71599	a16.ch35@g.chuo-u.ac.jp	高桑 智就	10658	PC2-012
71600	kazuya@kuchem.kyoto-u.ac.jp	大坪 主弥	10649	2Aa-01
71601	daiki2502-2385@g.ecc.u-tokyo.ac.jp	阿久津大貴	10106	3Fa-05
71602	okazaki-takashi619@g.ecc.u-tokyo.ac.jp	岡崎　尚志	10079	PB1-014
71603	kei16uni@stu.kanazawa-u.ac.jp	笠原 渓介	10328	PE2-008
71604	ishida.riku@g.mbox.nagoya-u.ac.jp	石田 陸	10162	PA2-070
71605	sc0066hh@ed.ritsumei.ac.jp	チョウユウヨウ	10441	PE2-009
71606	nakamura-k@chem.s.u-tokyo.ac.jp	中村　一輝	10593	PF2-023
71607	y.hara.861@stn.nitech.ac.jp	原善邦	10590	PA2-009
71608	keita.sato.q1@dc.tohoku.ac.jp	佐藤啓太	10243	PD2-009
71609	ito-tsuyoshi@akane.waseda.jp	伊藤　武	10381	PA2-071
71610	basudev@bio.titech.ac.jp	Basudev Maity	10482	3E-08
71611	asantria@chem.sci.osaka-u.ac.jp	Anas Santria	10151	3B-02
71612	liguanping@g.ecc.u-tokyo.ac.jp	GUANPING LI 	10684	PA2-024
71613	6120021h@st.toho-u.jp	花香 敦也	10673	PA2-062
71614	langitc19@chem.sci.osaka-u.ac.jp	Langit Cahya Adi	10075	3B-03
71615	s1840216@ems.u-toyama.ac.jp	柴原　一綺	10605	PA2-048
71616	m206592@hiroshima-u.ac.jp	国米航大	10682	3Ab-07
71617	1321627@ed.tus.ac.jp	森 悠眞	10592	PA1-046
71618	yonezu.akira@f.mbox.nagoya-u.ac.jp	米津 章	10179	PF2-038
71620	tsunekawa-eisuke218@g.ecc.u-tokyo.ac.jp	恒川 英介	10247	3Aa-07
71621	tashiro.makoto@f.mbox.nagoya-u.ac.jp	田代 真	10100	PA1-047
71622	kumagai.keita@e.mbox.nagoya-u.ac.jp	熊谷 啓太	10186	PA2-049
71623	yupengW@ees.hokudai.ac.jp	王宇鵬	10610	PA2-074
71624	h_yamamoto@c.s.osakafu-u.ac.jp	山本　大貴	10666	2D-02
71625	ohara.koutarou.47m@st.kyoto-u.ac.jp	小原　広太郎	10369	2Aa-07
71626	s21g558@kagawa-u.ac.jp	杉山　歩	10481	PB2-007
71627	natsuki.taira.560@s.kyushu-u.ac.jp	多伊良夏樹	10437	PC2-013
71628	ohara.tomo.025@s.kyushu-u.ac.jp	大原 朋	10695	PF2-039
71629	m20tc040@ab.osaka-cu.ac.jp	向井美樹	10630	2B-02
71630	konoc7499@eis.hokudai.ac.jp	佐々木この	10601	4Ab-06
71631	onishi-k@iis.u-tokyo.ac.jp	大西航平	10690	2Ab-03
71633	pwd026u6@s.okayama-u.ac.jp	HAYIBOR, Kennedy Mawunya	10665	PA2-010
71635	tagami.y.ac@m.titech.ac.jp	田上 優	10694	PA2-063
71636	t-ohata@mtr.osakafu-u.ac.jp	大畑　考司	10679	3Aa-03
71637	kento_kosugi@chem.eng.osaka-u.ac.jp	小杉健斗	10689	3C-04
71638	sakaguchi-t@chem.s.u-tokyo.ac.jp	坂口 大輝	10687	PA2-064
71639	aoki-yun@iis.u-tokyo.ac.jp	青木 佑奈	10309	3Fa-07
71640	kawakami@organomet.chem.es.osaka-u.ac.jp	川上 友美	10284	2Ab-11
71641	helibnnaalclkvcu@stu.kanazawa-u.ac.jp	今井 裕也	10427	PA2-065
71642	sd202022@cis.fukuoka-u.ac.jp	松田雄太郎	10667	2Fb-04
71643	yuexin@chem.s.u-tokyo.ac.jp	Yue XIN	10466	PA2-025
71644	s2170029@ipc.fukushima-u.ac.jp	染野雄斗	10373	PC2-014
71645	saito.tomoya.r1@elms.hokudai.ac.jp	斎藤朋也	10231	4Ab-05
71646	206d1317@st.kumamoto-u.ac.jp	平山晴香	10609	PA2-026
71647	kohei.yamagami@oist.jp	山神 光平	10490	PB2-008
71648	n-eguchi@imr.tohoku.ac.jp	江口　尚輝	10317	PA2-027
71649	mizuki.saito.r4@dc.tohoku.ac.jp	齋藤 瑞己	10707	2D-07
71650	s-yokomori@issp.u-tokyo.ac.jp	横森創	10202	PB1-013
71651	hattori.fu@b.mbox.nagoya-u.ac.jp	服部 楓	10139	PA1-072
71653	k002080@kansai-u.ac.jp	徐　暁	10432	PA2-011
71654	20924001@edu.cc.saga-u.ac.jp	郡 大心	10693	PA2-042
71656	2133310139e@kindai.ac.jp	田中  啓裕	10565	PA2-073
71657	yamada.minoru.061@s.kyushu-u.ac.jp	山田　実	10702	PF1-005
71658	b018vcv@yamaguchi-u.ac.jp	知念　真妃郎	10168	PF1-006
71659	egi@ms.ifoc.kyushu-u.ac.jp	江木晃人	10448	PD2-010
71660	shubham.deolka2@oist.jp	Shubham Deolka	10714	2D-03
71661	m20sb022@dt.osaka-cu.ac.jp	長崎 海	10580	PD2-011
71662	imoto@chem.s.u-tokyo.ac.jp	井元 健太	10312	4Fa-03
71663	20nm025a@vc.ibaraki.ac.jp	津金 聖和	10639	PE2-010
71664	1320528@ed.tus.ac.jp	小畑広洋	10642	2Ab-10
71665	1320592@ed.tus.ac.jp	樋口　直	10573	4Ab-03
71666	7119001k@st.toho-u.ac.jp	北清　航輔	10631	2Aa-11
71667	liust@iis.u-tokyo.ac.jp	Liu SHAOTING	10554	2D-08
71668	yasunobu.wakafuji.a14@s.kyushu-u.ac.jp	若藤恭暢	10712	3Fb-05
71669	sugiarto@hiroshima-u.ac.jp	Sugiarto	10634	PA2-066
71670	t2133063@edu.cc.uec.ac.jp	高野 莉奈	10583	2B-10
71671	kaito.hirakawa.s1@dc.tohoku.ac.jp	平川海斗	10464	3Aa-01
71672	nakaya@josai.ac.jp	仲谷学	10710	PF2-024
71673	a17.es3w@g.chuo-u.ac.jp	田端 隼人	10711	PF1-007
71674	df303002@edu.osakafu-u.ac.jp	宮﨑 祐輔	10194	PD2-012
71675	yan.xin.050@s.kyushu-u.ac.jp	Yan Xin	10655	3Fb-06
71676	shimada.t.an@m.titech.ac.jp	嶋田 光将	10616	PA1-048
71677	g865002h@mails.cc.ehime-u.ac.jp	瀧本 和誉	10359	PF2-025
71678	s20cm06sr@ous.jp	新谷　倫	10686	PB2-009
71679	c5620045@aoyama.jp	山本 侑貴奈	10720	PA1-019
71680	2133310105x@kindai.ac.jp	小阪　空	10304	PA2-028
71681	s212892m@st.yamagata-u.ac.jp	武藤匠海	10675	PB2-010
71682	6121001a@st.toho-u.jp	新井　駿祐	10507	PA1-049
71684	ji.conghao.919@s.kyushu-u.ac.jp	冀　聰昊	115097	PF2-016
71685	hanjunyi@chem.eng.osaka-u.ac.jp	Junyi HAN	10636	2Ab-14
71686	215d8108@st.kumamoto-u.ac.jp	平 尭宏	10569	PA2-029
71687	s212117m@st.yamagata-u.ac.jp	伊藤暖	10570	PB1-012
71688	mitsuhashi@staff.kanazawa-u.ac.jp	三橋了爾	10721	2Aa-10
71689	kikunaga.ryoma.437@s.kyushu-u.ac.jp	菊永 竜馬	10698	PF2-017
71690	20nm209t@vc.ibaraki.ac.jp	島 悠人	10691	PE2-011
71691	usov.p.aa@m.titech.ac.jp	Usov Pavel	10723	2Aa-05
71692	tattu622@stu.kanazawa-u.ac.jp	野本 竜矢	10623	PB1-011
71693	natsumi@riko.shimane-u.ac.jp	矢野 なつみ	10488	PA2-054
71694	mineo-y@chem.s.u-tokyo.ac.jp	峯尾 侑希	10330	PF2-026
71695	a15.6nfx@g.chuo-u.ac.jp	水谷 友裕	10704	PB2-011
71696	kuge.keita.096@m.kyushu-u.ac.jp	久家　恵大	10653	4C-05
71697	tetsu.sato.r1@dc.tohoku.ac.jp	佐藤　鉄	10668	2B-03
71698	kan.masanori.956@s.kyushu-u.ac.jp	管　昌権	10524	3C-01
71699	1320587@ed.tus.ac.jp	野村 響佑	10127	2B-12
71700	yang.haoyu.405@s.kyushu-u.ac.jp	Haoyu Yang	10713	PF2-018
71701	lianghao_007@outlook.com	Hao Liang	10556	PA1-050
71702	d201480@hiroshima-u.ac.jp	土屋　直人	10597	4Fa-07
71703	y-shigeta@se.kanazawa-u.ac.jp	重田　泰宏	10076	PA2-016
71704	maeda.akari.552@s.kyushu-u.ac.jp	前田　朱里	10046	PA2-032
71705	wada.y.am@m.titech.ac.jp	和田　雄貴	10708	2Aa-06
71706	huang.pingping.58x@st.kyoto-u.ac.jp	Pingping HUANG	10555	2B-06
71707	a17.5xat@g.chuo-u.ac.jp	髙橋 拓未	10606	PF1-008
71708	ishimori.s.ab@m.titech.ac.jp	石森俊哉	10250	PA2-017
71709	kentaro.fuku.q5@dc.tohoku.ac.jp	福健太郎	10692	3B-04
71710	m205703@hiroshima-u.ac.jp	廣野　恵大	10718	4Fa-08
71711	219d9031@st.kumamoto-u.ac.jp	禅野 光	10626	2B-13
71712	maeda.koshi.681@s.kyushu-u.ac.jp	前田晃志	10696	PC2-015
71713	mc21008@shibaura-it.ac.jp	臼井大智	10717	PA1-051
71714	2033320217b@kindai.ac.jp	池田 健介	10591	PA2-018
71715	yuto.sakaguchi.244@s.kyushu-u.ac.jp	坂口雄人	10654	3C-02
71717	mh1043@wakayama-u.ac.jp	古川　裕太	10260	PA2-012
71718	215d8111@st.kumamoto-u.ac.jp	中村　陸人	10705	2Aa-09
71719	1321517@ed.tus.ac.jp	猪熊究	10699	2B-11
71720	hikaru_iwami@chem.eng.osaka-u.ac.jp	石見輝	10727	PC2-016
71721	2133310112x@kindai.ac.jp	田中悠希	10563	PF1-009
71722	mc21017@shibaura-it.ac.jp	實方　友輝	10716	PD2-013
71723	ikeda-y@chem.s.u-tokyo.ac.jp	池田 侑典	10251	PF1-010
71724	a15.xjgs@g.chuo-u.ac.jp	今泉 暁	10726	PF2-019
71725	donoshita@ssc.kuchem.kyoto-u.ac.jp	堂ノ下将希	10501	2B-07
71726	1944320201n@kindai.ac.jp	梶原　悠	10728	PA2-019
71727	sekine@kumamoto-u.ac.jp	関根良博	10709	2B-14
71728	az.ryo.chemi@gmail.com	東　亮介	10725	PF2-028
""".splitlines()

#2021-08-18 removed by request
#71716	cliuses@gmail.com	坂倉広也	10681	PF2-027


roomtypes = set()

pid = {}
for line in data:
    cols = line.split("\t")
    if len(cols) > 4:
        # print(cols[0], cols[4])
        code = cols[4]
        if code[0] == "P":
            code = code[0:4] + code[5:]
        room = code[:code.find("-")]
        if room not in roomtypes:
            roomtypes.add(room)
        pid[cols[0]] = code

for room in sorted(list(roomtypes)):
    print(room, file=sys.stderr)



master = json.load(sys.stdin)
for id in master:
    master[id]["code"] = pid[id]

print(json.dumps(master, indent=4, ensure_ascii=False))
