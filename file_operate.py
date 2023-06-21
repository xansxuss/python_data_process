import os,shutil,argparse

# source = '/home/xanxus/Desktop/HaGRID_data/data/label/anno_xml_stop'
# target ='/home/xanxus/Desktop/HaGRID_data/t/stop/xml/'
source = '/home/xanxus/Desktop/number_data/digit_6'
target ='/home/xanxus/Desktop/number_data/NG'
name_list=[ '1898_jpg_rf_6197173974813bfa6a7fe4757792f675', '447_jpg_rf_f881ff87a2d90771348f0ca7357c8009', '1647_jpg_rf_878f5746d28f38580b831b0828e8a930', '409_jpg_rf_15d72900bddf984854186978ebf0d052', '465_jpg_rf_fc242d558e05dc2c1f350e9b506ee1fa', '513_jpg_rf_1ffd0338f9b084c91e5318f196b65af8', '1825_jpg_rf_9c49c81663dbb46df49db5484003d5d5', '1778_jpg_rf_d13c2dc593aebf09b12fbe718ca5bcf5', '839_jpg_rf_f61e8d9c4120d937aa45712747f2135b', '663_jpg_rf_d48a72941f860e07ea6724a3aaf92d0a', '1450_jpg_rf_920b3ee1cfd1a7605a6f02b914c06b62', '965_jpg_rf_0342b0c5d275ed0c605bb5158afd28de', '403_jpg_rf_76661ab460e8c31c89a271f94f2ca000', '1558_jpg_rf_84739222331652d7413e588125f494e2', '559_jpg_rf_201798015fa5de3d42239e6937afd67a', '340_jpg_rf_95900926bbf30b60ba38c1064eb2304b', '1495_jpg_rf_a893a27890843317083e508d94cb3d8f', '931_jpg_rf_ed7881b0185ad75c9184ec46e3fb7833', '1697_jpg_rf_1efb633dd4fa040a6f4bfc3b4a559c37', '1396_jpg_rf_4ade944fa3a1c9f00c930e7916d2427f', '851_jpg_rf_850020104fe9aa1192c8be76de9ed7b0', '1367_jpg_rf_9cd6140515c6698a38e49f93e8f8fffa', '1562_jpg_rf_d536eab301bf801f6124ae021cf31b54', '1080_jpg_rf_3a050d7a8332a2930d344f0a9106807e', '1791_jpg_rf_d3f8d03d21518c56855f61fb22011860', '1489_jpg_rf_8dcbde681895a0af4e6cad0536872324', '243_jpg_rf_3ebc7b05fe805421e1102122a4b3cd41', '1773_jpg_rf_2677ec8e17640077a8a032b750f932e2', '1459_jpg_rf_0c5bd5df1c40d086a8f314b0d12c2aac', '1985_jpg_rf_91fc221bddec4e3f414c4df2e95963e1', '761_jpg_rf_9a21c9800d831534db065fbb5ea0b976', '1534_jpg_rf_91629b5af873abd957abf20b1b6a3489', '1315_jpg_rf_b20019a703fae82af476c3efaa7c8cce', '1714_jpg_rf_167569162916a7d8ce673d926eec8182', '1851_jpg_rf_a532e0614b860ad27b2f84a32dc38382', '310_jpg_rf_88db2eaf1cadd7a2063ca59e0f71296f', '983_jpg_rf_4e2aa1d961ca08d5f7bde655bfb9b9da', '1503_jpg_rf_894cbe85eab3758eda7c08e4c444bf46', '633_jpg_rf_4974c1ebcad9a2e5f4797e26b449d01e', '643_jpg_rf_76b22463d32b637015f7f34644e02387', '650_jpg_rf_544e5a093d5defb3aa257d5179477c0b', '298_jpg_rf_81d3e0875519a0eb00d94a781828145d', '1822_jpg_rf_f88db5c066d2f6d2da5863c9f6c5f23c', '1927_jpg_rf_d048eec9f395b8660c20d3e6b809833c', '1500_jpg_rf_e45576bc5161c8227833fd3087551f7e', '1821_jpg_rf_469f439a1ebb1f04a9e1973c85ccc1f2', '1524_jpg_rf_052054d5896eded5a9b9bc0e8b68d430', '426_jpg_rf_29a355af5040b2a2c0720fa8d1ebe4b2', '1764_jpg_rf_64cc372f1ce73548cfe73a3a4ebd734c', '183_jpg_rf_cf6b111154daebbad687a69f2b78263b', '1943_jpg_rf_254b6b4318e99d292c9d0f768667472a', '711_jpg_rf_4e35e3f206ae5e58139da65996bd3a98', '1279_jpg_rf_b8d99a65cbb9030c5925efc5b32e23b3', '1474_jpg_rf_c598bd267dec1b856024ee2b97ab8897', '718_jpg_rf_963218862aa2760c8fdbdcede5cdec49', '603_jpg_rf_172c674bf60ebd591cf2aa11eca2bbea', '1916_jpg_rf_182cc61ba346766cd38d129391fcb102', '520_jpg_rf_110e1296d537d6b79a78ae6cca1dc901', '568_jpg_rf_ea9b26ae15b437b28fc564fedf4433f7', '1845_jpg_rf_d490fcc1e43468b32c3355ca2da6df85', '492_jpg_rf_106e0d49d7dcd075f5350aa8180899e7', '1467_jpg_rf_ce91141a0bc4e09d55fc2d479f7f0e77', '1441_jpg_rf_259c6a86a9addd907b89057def7021a8', '193_jpg_rf_ac824c48253ca88b04d807e750a5512e', '1818_jpg_rf_9b547fc8d6368a4de48d3ce292359d89', '1552_jpg_rf_f97dd5b9402ca35a8df92fda2b5633be', '1075_jpg_rf_7af43c60f7aadab2db4e872c3b780ac1', '1699_jpg_rf_6e0424f321e7c217fbca11316aa172bc', '1917_jpg_rf_6f3ba7c77f60eceb620904e3369de9cd', '641_jpg_rf_434e08fe50386ddcc7419ea637636fb9', '1268_jpg_rf_8b29f3975c0c214795681d180ac32339', '1428_jpg_rf_c3a3b0a934c2de3c007f8a02777ba09c', '297_jpg_rf_100079e46f028f8ca5d1ee7982b2a87e', '1864_jpg_rf_8f93cdd4315ec8c453416a262f64a61c', '1244_jpg_rf_da4c1e2a5c9fe76788bd415eb7cb67c0', '756_jpg_rf_634722ec552394733e7bc7225da31b91', '335_jpg_rf_fd5046c770b79c854684c61027718c1a', '204_jpg_rf_f26d043ed342b7a4a99ad99e8c250091', '1717_jpg_rf_cdf4df9a064ba71c89f35b7f2e2c7d5b', '532_jpg_rf_eea85888bfb83774ff3ca3c4d3b334ef', '512_jpg_rf_17b0b701a446cb57989dbf051ec53a11', '218_jpg_rf_99fb9a9aa1069cd959815e35f440b403', '536_jpg_rf_1c253d4354207ed2da984a84e80fb64f', '1527_jpg_rf_bbf5aa79ec470c82478a96eb2e9295db', '534_jpg_rf_03923feeb3ed68958d2ad2c1b360ae8a', '731_jpg_rf_25cdf24828cdf6ad2b81e86c08c213e7', '1392_jpg_rf_2ef7f54fbb5e644be335fb29a312e812', '428_jpg_rf_2b676329b77dc154f64a48699501336a', '510_jpg_rf_40c9e8d92c10742225410b88cdb23c8e', '1566_jpg_rf_13700bf4251d8b0be09c7e9bee28054f', '1881_jpg_rf_442e3434c536fa9778b0948892bb5e55', '1453_jpg_rf_22ca5c27e3f303313945b7ea762c721e', '574_jpg_rf_d78cdba3c58bc421b6eb84c94695d3da', '1750_jpg_rf_292bfe8b480ff44d3f593a3009bcc227', '1440_jpg_rf_28a8faabf2a8ffa509447a7cdefc1472', '345_jpg_rf_978986260b88e34e2750cb8837a3d191', '336_jpg_rf_364575c977a268ae6553bacb759f577c', '930_jpg_rf_ff88fec052f3ce8b62f1882b93b1af01', '251_jpg_rf_61a27412d72ddc1461fe911f6fdad529', '1498_jpg_rf_5aaa7d4b6c8efb0519f0f95a5689e53e', '1897_jpg_rf_29d896f751193ec8ff895c13ea445d64', '1693_jpg_rf_994f38e56f7044633e29c64b45b2aa26', '1982_jpg_rf_f76903d92f102a112bb90c3aa491876f', '530_jpg_rf_8e71b7711abea172101d4653e6e1bc9e', '1499_jpg_rf_5eaee520b19a478f021a72d198defd43', '1696_jpg_rf_a1b77965451dd51a4909439b467c14de', '997_jpg_rf_906498777aeb8c05ded0e3eae4bad71e', '1918_jpg_rf_c5c2a096071293888d8038c12f068f93', '1767_jpg_rf_bc3142df6e64af3290c00e67f9ba1c29', '269_jpg_rf_885e8f9f3c0707dec49bdd423ffbcee4', '553_jpg_rf_166aeae5d9638bb4022f99a9361bfc1e', '288_jpg_rf_8ba234404029bede640ee22d5ca709de', '346_jpg_rf_9c7e45c8e00a5f6e39373268dc0df93a', '168_jpg_rf_1272ec6ac0b7b04d7a478f44b040293d', '135_jpg_rf_e4e3fd98204a19e27f8ad70fa613be77', '1519_jpg_rf_a9df08cdb12e7cda96848a0d4151c853', '1690_jpg_rf_74b833e1369c471dbd315c62e326252c', '1439_jpg_rf_abb4ac822c6457c3926b386f494f6f2d', '1502_jpg_rf_994e2a77dc5938cf56c2b2596891ceae', '209_jpg_rf_2d58677948366251999a5a227132cdce', '178_jpg_rf_9056d5f84b8b47d753f7a6622cfcee1c', '684_jpg_rf_a6cea0a3f6a48999c60c3f2a2de69ce4', '850_jpg_rf_2ea40fb4671faac4c4e7cb0b7e124a7f', '337_jpg_rf_77d9bee7e535259711983fa87f07a4ee', '1445_jpg_rf_6ad58282ddede57208d790784fbf72e5', '1466_jpg_rf_2b90b6a8bb6ae73b5ea3ab4f5212d8c3', '644_jpg_rf_3eb8d9bd4f8d0dc37d1a15008fb6dc89', '1849_jpg_rf_a9dfbc343291b42ad52a5c2a493f59a2', '968_jpg_rf_ebfea109c18e6c08338db6c56ec0b404', '174_jpg_rf_0d90d97a530e569e393c0f8b58bc1e16', '331_jpg_rf_43fecca008974713c9c35b30812cc0a5', '184_jpg_rf_31b293ecfdfca4fb53a93323503d109d', '1042_jpg_rf_c124e8a589deac947d4f9a483d2f170b', '1485_jpg_rf_0ad9834a30f00a425744780538d54ff8', '1477_jpg_rf_67b3f127c109e85f96a371c7427d3201', '1876_jpg_rf_559635a42ca6b20c39cd36218bdb3c54', '1449_jpg_rf_b0ffe22d3a9693478787a280bf6fdf02', '86_jpg_rf_6227807aa8e919cf76238f2afb26eebb', '446_jpg_rf_0a47d0fecd4a1b3dcb20390670c3e8c5', '1625_jpg_rf_a33d74c111c04238ba41374f67a23c4c', '766_jpg_rf_a4a044c72887bef6738a8ca99414b229', '560_jpg_rf_9adcd7e3bb5c263b59c32f4f58614da1', '1516_jpg_rf_fc73aee00feaab837f46bc9237bf01ef', '730_jpg_rf_9c911dc0247514c2322303574fe14812', '608_jpg_rf_62d67b1831c3cf332588ac4b7cb24c5c', '964_jpg_rf_27ed644b96487e8650b68a81b87f10a8', '1617_jpg_rf_c2de1676d1ee14f508590092fc5dd464', '987_jpg_rf_7b157f30b25a1cb82eb036d3aa006257', '1196_jpg_rf_eaeff27629fadbf5eadde6516c365d4b', '1460_jpg_rf_7e7a8876e3cbb32b6f17fc5f17e8e9fc', '1685_jpg_rf_1437b9589c9ab1fd3dbec1b9d5e32764', '1830_jpg_rf_4e4675349391cbd06e2ba38e5811d7f6', '660_jpg_rf_b5c35eea811804bd413e4ea1a72c3d81', '966_jpg_rf_4381618104fcd7004ce11a13b83e50a2', '444_jpg_rf_a1f71e3d3930a4a8e7bd7d5f25344320', '402_jpg_rf_d864f194876f6471e8ae228f96d4136d', '290_jpg_rf_22048b1753de12af153cf14a09a7a949', '1874_jpg_rf_9d809ec9f3a7b248dcb5abf3ff21999a', '1718_jpg_rf_16cca3a37c9170eedbbb49527fa61901', '1862_jpg_rf_63af5b19cd4ff497e1c71efa9506e429', '735_jpg_rf_2a406dbe76b5c17186c9d4204dca7f4c', '1304_jpg_rf_d8a858a18a7e78a61ad8fedc4ad50491', '814_jpg_rf_87878c82c6954ec14a82582a919a58ab', '356_jpg_rf_527ce1a39e4caa6e66558813deec5613', '948_jpg_rf_e18574c770c3833249c725e6ab7f55a2', '450_jpg_rf_5d309a33f8d0bf0a1c49603a34f17f22', '685_jpg_rf_adf6773ac16bc35267419189b60ccf9a', '1817_jpg_rf_347ed73fcdb0fee98a4f07e9bf9d2b23', '812_jpg_rf_ceeebefec0c4a6f259fe5be4911edd14', '437_jpg_rf_48b0c0d534b7ee2340bf627098a5c785', '539_jpg_rf_0bb9979d8a77496fdcf175c19b641c56', '425_jpg_rf_8f94561df31339b329bf3a7ad76cff3f', '811_jpg_rf_1edf9f8ce68c94e2336fbde42a9232cd', '1831_jpg_rf_99e7ac599ec0d04a86d048b93979d061', '1486_jpg_rf_8015a71d753c6d980e61852ca2b19978', '9_jpg_rf_7dbbcb4a95b661b859f71db700979959', '727_jpg_rf_5812ffd581d63e58b8e040612bc3a0c8', '740_jpg_rf_cdbb466aa013de9bd472e46896b2cd1c', '1544_jpg_rf_f7016ae55279619da010f07c1d0bea61', '1530_jpg_rf_bc45a76a774b52fb97c046317ee2e14b', '320_jpg_rf_a1525235b203fd123a7a2327e999378b', '1709_jpg_rf_3035e86e341b198d8eb4105d89e34a49', '1573_jpg_rf_d2b78afdf8c9e7feb2c73a4058238442', '828_jpg_rf_f1d1e2acf694206877fa0c08088f4321', '687_jpg_rf_4133abfba36689f83ced7eb753a967ab', '1475_jpg_rf_0af9e3240df0404f6c57a80107e5f76a', '1161_jpg_rf_3d872f51210f6330f8322e7f29549a67', '1509_jpg_rf_19cb70020cb7d13a54f8568cba671e24', '329_jpg_rf_08e91d9d38386d4860cf51015c92f488', '863_jpg_rf_a2be618205c49e12a3e929702c5d72ab', '646_jpg_rf_97bc2ac304bb570145be62356ba485cd', '324_jpg_rf_a3b0669386c6d9cc98557f4d0d3f2abd', '762_jpg_rf_b5486027a46eece651116a004dfd8b8d', '544_jpg_rf_08d8e6912c4928000169c9e589605e03', '1471_jpg_rf_fef5fac86c617ced63636614b181b0f3', '424_jpg_rf_e3b725d107fc3ff3620ca2437a09db97', '414_jpg_rf_8c5734ebb5e4f41800be1699c7f8ec24', '755_jpg_rf_2f00c9150c25ca08085576f6da72beb4', '1847_jpg_rf_ae3eb44351feb3501f0b68f3f4df3982', '312_jpg_rf_2e485b57e935d56db41cf7362aa8a8a4', '365_jpg_rf_9ab460c9f2091cb76cecd8c15f42300d', '977_jpg_rf_f31d14822136b62f9b84911fc5792be4', '969_jpg_rf_e88db06a83c348e844073ce4d0a5cb44', '489_jpg_rf_93e7f20d360afb5006614544160c9fe4', '205_jpg_rf_3d439bb5e6936f78a4471735c53579b6', '1403_jpg_rf_3ede365350bf5f3cf5045e02ccd4d894', '191_jpg_rf_2f5d102582910d80995a5ec8edaab5ee', '729_jpg_rf_aaee0decc527544e68d6cc157f96095d', '635_jpg_rf_27baacddc3e3562b2c8d511f26d402c4', '1735_jpg_rf_904b8ef7758180ca902d74b316c1b1e6', '1976_jpg_rf_a60ed440749bf73a2c30afb3e5564ace', '709_jpg_rf_9465ea3bf3764567623bbfd9b883d188', '1451_jpg_rf_e5c93c1025e811a0edb9ed3c6a9c167a', '1494_jpg_rf_4d00b49c9423ff0dea8a13e7c2287e8b', '769_jpg_rf_e2d507919acb80f4011358ed21f99c64', '1537_jpg_rf_dce9b5d48812db33ff63f006f30fc051', '352_jpg_rf_fe414bb3ecdab2d41c7eb06d1119ed9b', '1824_jpg_rf_419f74bf078a55a44c59f9b30cd2035b', '1452_jpg_rf_7ed7c1e6ac3f572de94303618b0371a4', '508_jpg_rf_ea98244932b2a878f42ac775fa7fb9bc', '511_jpg_rf_7f7f0b19d6249a612daa6a3731414946', '1564_jpg_rf_0012e4c10f63841109559acfe70b6716', '715_jpg_rf_b6ae5e6ab0edfa671f5612ceb14de767', '1444_jpg_rf_e19c3897829f1cf1cfa290b896a961c9', '317_jpg_rf_3f5e730d75ace42596d76c90d6cc1b91', '543_jpg_rf_ac761b62c5ba47f8f242c9a06808ffb9', '1930_jpg_rf_b966b47ae5cb3abfcab08541ea5ebb80', '494_jpg_rf_adcb1d6d15fc383431bddaabbd45443c', '507_jpg_rf_651b7166ba8bce4f510f927d5389bd2e', '427_jpg_rf_ea2f27d2e278d32cc70ca9a42e666fd7', '238_jpg_rf_3842790d7e4148a02993a6d5fbf1cc8a', '1087_jpg_rf_71238290b7cd4d75641a2893a595dcda', '1572_jpg_rf_8887cb46c4d62f98191d35810599b364', '327_jpg_rf_1c7b92d9a74c6a53c2cfd1c1b71b6ab1', '105_jpg_rf_578261494279c648698962bba7139e39', '1723_jpg_rf_8c33819350bc3540b060f0ee33d0df56', '1404_jpg_rf_9bc415f2574396590e7e2de276a6af28', '872_jpg_rf_a6ddfda933f3f5b09a059c4cdc23dfee', '1736_jpg_rf_d29572aecf64b6b6e0cbbf7933d51372', '1983_jpg_rf_d1a5fd50abef3bb259d59db041974864', '1899_jpg_rf_3f775f0fddf15edc0c70fe050c30f54a', '1518_jpg_rf_deb84e72f64c7737e8d767cd2f27e069', '449_jpg_rf_f603a88c32d789f0d876db1434a453fe', '1921_jpg_rf_da4a17791228408e25e53a1106cedccd', '1593_jpg_rf_1932213a62aad15ceaa301f96423a4d5', '1563_jpg_rf_077e9b8aaefa2ae0ddd2711415ab2f5e']
def get_file(path):
    file_list=[]
    files=os.listdir(path)
    for i in range(len(files)):
        if '.' in files[i]:
            name=files[i].split('.')[0]
            file_list.append(name)
        else:
            # print("it is folder")
            continue
    return file_list

def move_f(file_name ,ex_name,source,target):
    # source=os.path.join(source,file_name)
    # shutil.move(source,target)
    shutil.move(os.path.join(source,'{}.{}'.format(file_name,ex_name)),target)
    # print(os.path.join(source,'{}.{}'.format(file_name,ex_name)))

def copy_f(source ,target):
    shutil.copy(source,target)

def get_extension(name):
    exname=name.split('.')[1]
    return exname
def decide_file_exist(name):
    if not os.path.exists(name):
        os.mkdir(name)    

def check_path(path):
    if not os.path.isdir(path):
       os.makedirs(path) 
def check_file_number(path):
    number = len(os.listdir(path))
    return number
def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--path",help="label path")
    known_args, _ = parser.parse_known_args()
    return known_args
if __name__ == "__main__":
    
    for i in range(len(name_list)):
        shutil.move(os.path.join(source,'labels','{}.xml'.format(name_list[i])),target)
        shutil.move(os.path.join(source,'imgs','{}.jpg'.format(name_list[i])),target)
    # args=parse_arguments()
    # ls = os.listdir(args.path)
    # for l in ls:
    #     n=l.split('.')
    #     if len(n)>2:
    #         print('name:{},split:{},len:{}'.format(l,n,len(n)))

    # img_l=get_file(os.path.join('/home/xanxus/Desktop/HaGRID_data/Dataset/stop','img'))
    # label_l=get_file(os.path.join('/home/xanxus/Desktop/HaGRID_data/Dataset/stop','label'))
    # out=list(set(img_l).symmetric_difference(set(label_l)))
    # print(out)