import re

def solve(doc):

    ####################################################################################################################
    ########################################## REMOVAL OF UNNECESSARY TOKENS ###########################################
    doc = doc.lower()
    doc = re.sub(r"\b\d+\b", " ", doc)
    doc = re.sub(r"(?<!\.)[\!\"\#\$\%\&\(\)\*\+\,\-\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]", " ", doc)
    doc = re.sub(r"(\ m{0,3}(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})(ix|iv|v?i{0,3}))|(m{0,3}(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})(ix|iv|v?i{0,3})\ )|(\ m{0,3}(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})(ix|iv|v?i{0,3})\ )", " ", doc)
    doc = re.sub(r"\b(\w)\1+\b", " ", doc)
    doc = re.sub(r"\b(\d)\1+\b", " ", doc)
    #==================================================================================================================#

    ####################################################################################################################
    ###################################### RESOLVING OFFICIALLY USED ABBREVIATIONS #####################################
    doc = re.sub(r"(\ crpc\ )|(\ cr\ p\ c\ )|(\ c\ r\ p\ c\ )|(\ cr\ pc\ )|(\ c\ r\ pc\ )", " crpc ", doc)
    doc = re.sub(r"(\ j\ )|(\ j\.)", " justice ", doc)
    doc = re.sub(r"(\ mr\.)|(\ mr\ )", " mister ", doc)
    doc = re.sub(r"(hon'ble)", " honourable ", doc)
    doc = re.sub(r"\(sc\)", " supreme court ", doc)
    doc = re.sub(r"\ sc\ ", " supreme court ", doc)
    doc = re.sub(r"(\ vs\ )", " versus ", doc)
    doc = re.sub(r"\ sr\ ", " senior ", doc)
    doc = re.sub(r"\ no\ of", " number of ", doc)
    doc = re.sub(r"\ ltd\ ", " limited ", doc)
    doc = re.sub(r"sdjm", " subdivisional judicial magistrate ", doc)
    doc = re.sub(r"\ govt\ ", " government ", doc)
    doc = re.sub(r"\ v\ ", " versus ", doc)
    doc = re.sub(r"\ scc\ ", " supreme court cases ", doc)
    doc = re.sub(r"\ nos\ ", " numbers ", doc)
    doc = re.sub(r"\ ors\ ", " others ", doc)
    doc = re.sub(r"\ pvt\ ", " private ", doc)
    doc = re.sub(r"\ anr\ ", " another ", doc)
    doc = re.sub(r"\ ilr\ ", "international law reports ", doc)
    doc = re.sub(r"\ nct\ ", " national capital territory ", doc)
    doc = re.sub(r"\ itr\ ", " income tax return ", doc)
    doc = re.sub(r"\ ito\ ", " income tax officer ", doc)
    doc = re.sub("r\ aac\ ", " administrative appeals chamber ", doc)
    doc = re.sub(r"\ arc\ ", " administrative reforms commission ", doc)
    doc = re.sub(r"\ dr\ ", " doctor ", doc)
    doc = re.sub(r"\ misc\ ", " miscellaneous ", doc)
    doc = re.sub(r"\ cb\ ", " common bench ", doc)
    doc = re.sub(r"\ crl\ ", " criminal original petition ", doc)
    doc = re.sub(r"\ est\ ", " established in ", doc)
    doc = re.sub(r"\ air\ ", " all india reporter ", doc)
    doc = re.sub(r"\ cji\ ", " chief justice of india ", doc)
    doc = re.sub(r"\ cj\ ", " chief justice ", doc)
    doc = re.sub(r"\ jt\ ", " joint ", doc)
    doc = re.sub(r"\ sat\ ", " securities appellate tribunal ", doc)
    doc = re.sub(r"\ retd\ ", " retired ", doc)
    doc = re.sub(r"\ cas\ ", " cases ", doc)
    doc = re.sub(r"\ acc\ ", " accident and compensation cases ", doc)
    doc = re.sub(r"\ acj\ ", " accidents claims journal ", doc)
    doc = re.sub(r"\ aihc\ ", " all india high court cases ", doc)
    doc = re.sub(r"\ faj\ ", " all india prevention of food adulteration journal ", doc)
    doc = re.sub(r"\ allmr\ ", " all maharashtra law reporter ", doc)
    doc = re.sub(r"\ arc\ ", " allahabad rent cases ", doc)
    doc = re.sub(r"\ awc\ ", " allahabad weekly cases ", doc)
    doc = re.sub(r"\ alt\ ", " andhra law times ", doc)
    doc = re.sub(r"\ ald\ ", " andhra legal decisions ", doc)
    doc = re.sub(r"\ aplj\ ", " andhra pradesh law journal ", doc)
    doc = re.sub(r"\ anwr\ ", " andhra weekly reporter ", doc)
    doc = re.sub(r"\ ad\ ", " apex decision ", doc)
    doc = re.sub(r"\ arblr\ ", " arbitration law reporter ", doc)
    doc = re.sub(r"\ bc\ ", " banking cases ", doc)
    doc = re.sub(r"\ bljr\ ", " bihar law journal reports ", doc)
    doc = re.sub(r"\ bomcr\ ", " bombay cases reporter ", doc)
    doc = re.sub(r"\ bomlr\ ", " bombay law reporter ", doc)
    doc = re.sub(r"\ buslr\ ", " business law reports ", doc)
    doc = re.sub(r"\ chn\ ", " calcutta high court notes ", doc)
    doc = re.sub(r"\ callt\ ", " calcutta law times ", doc)
    doc = re.sub(r"\ cwn\ ", " calcutta weekly notes ", doc)
    doc = re.sub(r"\ civilcc\ ", " civil court cases ", doc)
    doc = re.sub(r"\ compcas\ ", " company cases ", doc)
    doc = re.sub(r"\ complj\ ", " company law journal ", doc)
    doc = re.sub(r"\ compat\ ", " competition law reports ", doc)
    doc = re.sub(r"\ cpj\ ", " consumer protection judgments ", doc)
    doc = re.sub(r"\ ctlj\ ", " contracts and tenders law journal ", doc)
    doc = re.sub(r"\ cla\ ", " corporate law adviser ", doc)
    doc = re.sub(r"\ crilj\ ", " criminal law journal ", doc)
    doc = re.sub(r"\ ccr\ ", " current criminal reports ", doc)
    doc = re.sub(r"\ ctc\ ", " current tamilnadu cases ", doc)
    doc = re.sub(r"\ ctr\ ", " current taw reporter ", doc)
    doc = re.sub(r"\ clt\ ", " cuttack law times ", doc)
    doc = re.sub(r"\ cwn\ ", " calcutta weekly notes ", doc)
    doc = re.sub(r"\ dlt\ ", " delhi law times ", doc)
    doc = re.sub(r"\ drj\ ", " delhi reported journal ", doc)
    doc = re.sub(r"\ dmc\ ", " divorce and matrimonial cases ", doc)
    doc = re.sub(r"\ esc\ ", " education and service cases ", doc)
    doc = re.sub(r"\ elr\ ", " energy law reports ", doc)
    doc = re.sub(r"\ ecc\ ", " excise and customs case ", doc)
    doc = re.sub(r"\ ecr\ ", " excise and custom reports ", doc)
    doc = re.sub(r"\ elt\ ", " excise law times ", doc)
    doc = re.sub(r"\ flr\ ", " factory law reporter ", doc)
    doc = re.sub(r"\ gld ", " gauhati law decisions ", doc)
    doc = re.sub(r"\ gaulr\ ", " gauhati law reports ", doc)
    doc = re.sub(r"\ glt\ ", " gauhati law times ", doc)
    doc = re.sub(r"\ glh\ ", " gujarat law herald ", doc)
    doc = re.sub(r"\ glr\ ", " gujarat law reporter ", doc)
    doc = re.sub(r"\ itr\ ", " income tax reporter ", doc)
    doc = re.sub(r"\ itd\ ", " income tax tribunal decisions ", doc)
    doc = re.sub(r"\ ilr\ ", " indian law reports ", doc)
    doc = re.sub(r"\ bom\ ", " bombay ", doc)
    doc = re.sub(r"\ jcr\ ", " jharkhand cases reporter ", doc)
    doc = re.sub(r"\ jkj\ ", " jharkhand judgments ", doc)
    doc = re.sub(r"\ jcc\ ", " journal of criminal cases ", doc)
    doc = re.sub(r"\ jt\ ", " judgment today ", doc)
    doc = re.sub(r"\ kccr\ ", " karnataka civil and criminal reporter ", doc)
    doc = re.sub(r"\ karlj\ ", " karnataka law journal ", doc)
    doc = re.sub(r"\ klj\ ", " kerala law journal ", doc)
    doc = re.sub(r"\ klt\ ", " kerala law times ", doc)
    doc = re.sub(r"\ labic\ ", " labour and industrial cases ", doc)
    doc = re.sub(r"\ llj\ ", " labour law journal ", doc)
    doc = re.sub(r"\ ls\ ", " law summary ", doc)
    doc = re.sub(r"\ mplj\ ", " madhya pradesh law journal ", doc)
    doc = re.sub(r"\ mlj\ ", " madras law journal ", doc)
    doc = re.sub(r"\ mhlj\ ", " maharashtra law journal ", doc)
    doc = re.sub(r"\ mipr\ ", " military interdepartmental purchase request ", doc)
    doc = re.sub(r"\ mia\ ", " moores indian appeals ", doc)
    doc = re.sub(r"\ mpht\ ", " madhya pradesh court today ", doc)
    doc = re.sub(r"\ myslj\ ", " madhya pradesh law journal ", doc)
    doc = re.sub(r"\ olr\ ", " orissa law reviews ", doc)
    doc = re.sub(r"\ ptc\ ", " patent and trade marks cases ", doc)
    doc = re.sub(r"\ plr\ ", " punjab law reporter ", doc)
    doc = re.sub(r"\ rlr\ ", " rajasthan law reporter ", doc)
    doc = re.sub(r"\ rlw\ ", " rajasthan law weekly ", doc)
    doc = re.sub(r"\ raj\ ", " rajdhani law reporter ", doc)
    doc = re.sub(r"\ rarj\ ", " recent arbitration judgments ", doc)
    doc = re.sub(r"\ rlt\ ", " revenue law times ", doc)
    doc = re.sub(r"\ stc\ ", " sales tax cases ", doc)
    doc = re.sub(r"\ scr\ ", " supreme court reports ", doc)
    doc = re.sub(r"\ scl\ ", " sebi and corporate laws ", doc)
    doc = re.sub(r"\ sot\ ", " selected orders of income tax appellate tribunal ", doc)
    doc = re.sub(r"\ sct\ ", " service cases today ", doc)
    doc = re.sub(r"\ stj\ ", " service tax journal ", doc)
    doc = re.sub(r"\ str\ ", " service tax review ", doc)
    doc = re.sub(r"\ slj\ ", " services law journal ", doc)
    doc = re.sub(r"\ slr\ ", " services law reporter ", doc)
    doc = re.sub(r"\ shimlc\ ", " shimla law cases ", doc)
    doc = re.sub(r"\ scale\ ", " supreme court almanac ", doc)
    doc = re.sub(r"\ scr\ ", " supreme court reporter ", doc)
    doc = re.sub(r"\ ttj\ ", " tax tribunal judgments ", doc)
    doc = re.sub(r"\ taxlr\ ", " taxation law reporter ", doc)
    doc = re.sub(r"\ stt\ ", " taxman service tax today ", doc)
    doc = re.sub(r"\ uj\ ", " unreported judgments ", doc)
    doc = re.sub(r"\ uplbec\ ", " uttar pradesh local bodies and educational cases ", doc)
    doc = re.sub(r"\ vst\ ", " vat and service tax cases ", doc)
    doc = re.sub(r"\ vr\ ", " vat reported ", doc)
    doc = re.sub(r"\ wln\ ", " weekly law notes ", doc)
    doc = re.sub(r"\ wlc\ ", " western law cases ", doc)
    doc = re.sub(r"\ pw\ ", " prosecuting witness ", doc)
    doc = re.sub(r"\ cw\ ", " cooperating witness ", doc)
    doc = re.sub(r"\ sec\ ", " section ", doc)
    doc = re.sub(r"\ mo\ ", " modus operandi ", doc)
    doc = re.sub(r"\ cri\ ", " confidential reliable informant ", doc)
    doc = re.sub(r"\ cr\ ", " crime ", doc)
    doc = re.sub(r"\ psi\ ", " pre sentence investigation ", doc)
    doc = re.sub(r"\ addl\ ", " additional ", doc)
    doc = re.sub(r"\ pws\ ", " performance work statement ", doc)
    doc = re.sub(r"\ {2,}", " ", doc)
    #==================================================================================================================#
    return doc

