# $ANTLR 3.1.1 FCL.g 2009-01-22 19:38:38

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import fuzzy.System
import fuzzy.InputVariable
import fuzzy.OutputVariable
import fuzzy.Adjective
import fuzzy.set.Polygon
import fuzzy.set.Singleton
import fuzzy.defuzzify
import fuzzy.defuzzify.Dict
import fuzzy.fuzzify
import fuzzy.fuzzify.Plain
import fuzzy.fuzzify.Dict
import fuzzy.operator.Not
import fuzzy.operator.Input
import fuzzy.operator.Compound
import fuzzy.Rule
import fuzzy.norm.Min
import fuzzy.norm.Max


def getNorm(name,p=None):
	"""Get an instance of a fuzzy norm with given name.
	Normally looks into the fuzzy.norm package for a suitable class.
	"""
	m=__import__("fuzzy.norm."+name,fromlist=[name])
	c=m.__dict__[name]
	if p is None:
		return c()
	else:
		return c(p)

def getDefuzzificationMethod(name):
	"""Get an instance of a defuzzification method with given name.
	Normally looks into the fuzzy.defuzzify package for a suitable class.
	"""
	m=__import__("fuzzy.defuzzify."+name,fromlist=[name])
	c=m.__dict__[name]
	return c()

# container for definitions of operator/norm pairs
_operators = {
	"AND":fuzzy.norm.Min.Min(),
	"OR":fuzzy.norm.Max.Max()
	}
	
def defineOperator(name,norm):
	"""Defines a operator (AND,OR,...) to use a given norm."""
	_operators[name] = norm
	#print "defineOperator ",name,norm
	
def getOperator(name):
	"""Get the norm for previous defined operator name."""
	#print "getOperator ",name
	import copy
	return copy.deepcopy(_operators[name])

_structs = {}

def defineStructType(name):
	"""Remember name of a struct definition"""
	_structs[name] = []

def defineStructTypeElement(name,elem):
	"""Add a struct element"""
	_structs[name].append(elem)

def getStructType(name):
	"""Get list of elements of a struct definition"""
	return _structs[name]



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
Real_literal=9
OR_=6
T__27=27
T__26=26
T__25=25
T__24=24
LETTER=10
T__23=23
T__22=22
T__21=21
T__20=20
AND_=7
EOF=-1
Identifier=4
T__55=55
T__56=56
T__19=19
T__57=57
T__58=58
T__16=16
T__51=51
T__15=15
T__52=52
T__18=18
T__53=53
T__54=54
T__17=17
Integer_literal_wo_sign=11
T__14=14
T__59=59
DIGIT=5
COMMENT=13
T__50=50
T__42=42
T__43=43
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
T__48=48
T__49=49
T__30=30
T__31=31
T__32=32
WS=12
T__33=33
T__34=34
Integer_literal=8
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "Identifier", "DIGIT", "OR_", "AND_", "Integer_literal", "Real_literal", 
    "LETTER", "Integer_literal_wo_sign", "WS", "COMMENT", "'FUNCTION_BLOCK'", 
    "'END_FUNCTION_BLOCK'", "'STRUCT'", "'END_STRUCT'", "':'", "'REAL'", 
    "';'", "'VAR_INPUT'", "'END_VAR'", "'VAR_OUTPUT'", "'FUZZIFY'", "'END_FUZZIFY'", 
    "'DEFUZZIFY'", "'END_DEFUZZIFY'", "'RULEBLOCK'", "'END_RULEBLOCK'", 
    "'OPTION'", "'END_OPTION'", "'TERM'", "':='", "'('", "','", "')'", "'METHOD'", 
    "'DEFAULT'", "'NC'", "'RANGE'", "'..'", "'['", "']'", "'MIN'", "'PROD'", 
    "'BDIF'", "'MAX'", "'ASUM'", "'BSUM'", "'ACT'", "'ACCU'", "'NSUM'", 
    "'NOT'", "'IS'", "'.'", "'RULE'", "'IF'", "'THEN'", "'WITH'"
]




class FCLParser(Parser):
    grammarFileName = "FCL.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)




               
        self.System = None




                


        

              
    # test



    # $ANTLR start "main"
    # FCL.g:87:1: main returns [system] : function_block_declaration ;
    def main(self, ):

        system = None

        try:
            try:
                # FCL.g:87:23: ( function_block_declaration )
                # FCL.g:87:25: function_block_declaration
                pass 
                #action start
                self.System = None;
                #action end
                self._state.following.append(self.FOLLOW_function_block_declaration_in_main45)
                self.function_block_declaration()

                self._state.following.pop()
                #action start
                system =  self.System
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return system

    # $ANTLR end "main"


    # $ANTLR start "function_block_declaration"
    # FCL.g:89:1: function_block_declaration : 'FUNCTION_BLOCK' function_block_name ( type_definition )* ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF ;
    def function_block_declaration(self, ):

        function_block_name1 = None


        try:
            try:
                # FCL.g:90:2: ( 'FUNCTION_BLOCK' function_block_name ( type_definition )* ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF )
                # FCL.g:91:3: 'FUNCTION_BLOCK' function_block_name ( type_definition )* ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF
                pass 
                self.match(self.input, 14, self.FOLLOW_14_in_function_block_declaration60)
                self._state.following.append(self.FOLLOW_function_block_name_in_function_block_declaration65)
                function_block_name1 = self.function_block_name()

                self._state.following.pop()
                #action start
                self.System = fuzzy.System.System(description=((function_block_name1 is not None) and [self.input.toString(function_block_name1.start,function_block_name1.stop)] or [None])[0]); 
                #action end
                # FCL.g:93:3: ( type_definition )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 16) :
                        alt1 = 1


                    if alt1 == 1:
                        # FCL.g:93:3: type_definition
                        pass 
                        self._state.following.append(self.FOLLOW_type_definition_in_function_block_declaration71)
                        self.type_definition()

                        self._state.following.pop()


                    else:
                        break #loop1


                # FCL.g:94:3: ( fb_io_var_declarations )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 21 or LA2_0 == 23) :
                        alt2 = 1


                    if alt2 == 1:
                        # FCL.g:94:3: fb_io_var_declarations
                        pass 
                        self._state.following.append(self.FOLLOW_fb_io_var_declarations_in_function_block_declaration76)
                        self.fb_io_var_declarations()

                        self._state.following.pop()


                    else:
                        break #loop2


                self._state.following.append(self.FOLLOW_function_block_body_in_function_block_declaration82)
                self.function_block_body()

                self._state.following.pop()
                self.match(self.input, 15, self.FOLLOW_15_in_function_block_declaration86)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_function_block_declaration91)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "function_block_declaration"


    # $ANTLR start "type_definition"
    # FCL.g:101:1: type_definition : 'STRUCT' Identifier ( struct_element[$Identifier.text] )+ 'END_STRUCT' ;
    def type_definition(self, ):

        Identifier2 = None

        try:
            try:
                # FCL.g:102:2: ( 'STRUCT' Identifier ( struct_element[$Identifier.text] )+ 'END_STRUCT' )
                # FCL.g:102:4: 'STRUCT' Identifier ( struct_element[$Identifier.text] )+ 'END_STRUCT'
                pass 
                self.match(self.input, 16, self.FOLLOW_16_in_type_definition103)
                Identifier2=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_type_definition105)
                #action start
                defineStructType(Identifier2.text); 
                #action end
                # FCL.g:102:64: ( struct_element[$Identifier.text] )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == Identifier) :
                        alt3 = 1


                    if alt3 == 1:
                        # FCL.g:102:64: struct_element[$Identifier.text]
                        pass 
                        self._state.following.append(self.FOLLOW_struct_element_in_type_definition109)
                        self.struct_element(Identifier2.text)

                        self._state.following.pop()


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                self.match(self.input, 17, self.FOLLOW_17_in_type_definition113)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "type_definition"


    # $ANTLR start "struct_element"
    # FCL.g:105:1: struct_element[struct_name] : Identifier ':' 'REAL' ';' ;
    def struct_element(self, struct_name):

        Identifier3 = None

        try:
            try:
                # FCL.g:106:2: ( Identifier ':' 'REAL' ';' )
                # FCL.g:106:4: Identifier ':' 'REAL' ';'
                pass 
                Identifier3=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_struct_element125)
                self.match(self.input, 18, self.FOLLOW_18_in_struct_element127)
                self.match(self.input, 19, self.FOLLOW_19_in_struct_element129)
                self.match(self.input, 20, self.FOLLOW_20_in_struct_element131)
                #action start
                defineStructTypeElement(struct_name,Identifier3.text);
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "struct_element"


    # $ANTLR start "fb_io_var_declarations"
    # FCL.g:109:1: fb_io_var_declarations : ( input_declarations | output_declarations );
    def fb_io_var_declarations(self, ):

        try:
            try:
                # FCL.g:110:2: ( input_declarations | output_declarations )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 21) :
                    alt4 = 1
                elif (LA4_0 == 23) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # FCL.g:110:4: input_declarations
                    pass 
                    self._state.following.append(self.FOLLOW_input_declarations_in_fb_io_var_declarations145)
                    self.input_declarations()

                    self._state.following.pop()


                elif alt4 == 2:
                    # FCL.g:111:4: output_declarations
                    pass 
                    self._state.following.append(self.FOLLOW_output_declarations_in_fb_io_var_declarations151)
                    self.output_declarations()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "fb_io_var_declarations"


    # $ANTLR start "input_declarations"
    # FCL.g:114:1: input_declarations : 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR' ;
    def input_declarations(self, ):

        try:
            try:
                # FCL.g:114:20: ( 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR' )
                # FCL.g:114:22: 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR'
                pass 
                self.match(self.input, 21, self.FOLLOW_21_in_input_declarations161)
                # FCL.g:114:34: ( var_decl[0] )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == Identifier) :
                        alt5 = 1


                    if alt5 == 1:
                        # FCL.g:114:34: var_decl[0]
                        pass 
                        self._state.following.append(self.FOLLOW_var_decl_in_input_declarations163)
                        self.var_decl(0)

                        self._state.following.pop()


                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1


                self.match(self.input, 22, self.FOLLOW_22_in_input_declarations167)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "input_declarations"


    # $ANTLR start "output_declarations"
    # FCL.g:115:1: output_declarations : 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR' ;
    def output_declarations(self, ):

        try:
            try:
                # FCL.g:115:21: ( 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR' )
                # FCL.g:115:23: 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR'
                pass 
                self.match(self.input, 23, self.FOLLOW_23_in_output_declarations175)
                # FCL.g:115:36: ( var_decl[1] )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == Identifier) :
                        alt6 = 1


                    if alt6 == 1:
                        # FCL.g:115:36: var_decl[1]
                        pass 
                        self._state.following.append(self.FOLLOW_var_decl_in_output_declarations177)
                        self.var_decl(1)

                        self._state.following.pop()


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                self.match(self.input, 22, self.FOLLOW_22_in_output_declarations181)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "output_declarations"


    # $ANTLR start "var_decl"
    # FCL.g:118:1: var_decl[output_var] : Identifier ':' type ';' ;
    def var_decl(self, output_var):

        Identifier5 = None
        type4 = None


        try:
            try:
                # FCL.g:119:2: ( Identifier ':' type ';' )
                # FCL.g:120:3: Identifier ':' type ';'
                pass 
                Identifier5=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_var_decl196)
                self.match(self.input, 18, self.FOLLOW_18_in_var_decl201)
                self._state.following.append(self.FOLLOW_type_in_var_decl206)
                type4 = self.type()

                self._state.following.pop()
                self.match(self.input, 20, self.FOLLOW_20_in_var_decl211)
                #action start
                 
                if output_var == 0:
                	var=fuzzy.InputVariable.InputVariable()
                	if type4 is not None:
                		# set fuzzification method to dictionary input
                		var.fuzzify = fuzzy.fuzzify.Dict.Dict();
                		# create adjectives for all struct members
                		for i in type4:
                			var.adjectives[i]=fuzzy.Adjective.Adjective(fuzzy.set.Set.Set())
                	else:
                		# default is the plain fuzzification
                		var.fuzzify = fuzzy.fuzzify.Plain.Plain();
                else:
                	var=fuzzy.OutputVariable.OutputVariable()
                	if type4 is not None:
                		# set defuzzification method to dictionary output
                		var.defuzzify = fuzzy.defuzzify.Dict.Dict();
                		# create adjectives for all struct members
                		for i in type4:
                			var.adjectives[i]=fuzzy.Adjective.Adjective(fuzzy.set.Set.Set())
                self.System.variables[Identifier5.text]=var;

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "var_decl"


    # $ANTLR start "type"
    # FCL.g:148:1: type returns [struct_type] : ( 'REAL' | Identifier );
    def type(self, ):

        struct_type = None

        Identifier6 = None

        try:
            try:
                # FCL.g:149:2: ( 'REAL' | Identifier )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 19) :
                    alt7 = 1
                elif (LA7_0 == Identifier) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # FCL.g:150:3: 'REAL'
                    pass 
                    self.match(self.input, 19, self.FOLLOW_19_in_type232)
                    #action start
                    struct_type =  None 
                    #action end


                elif alt7 == 2:
                    # FCL.g:152:2: Identifier
                    pass 
                    Identifier6=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_type240)
                    #action start
                    struct_type =  getStructType(Identifier6.text) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return struct_type

    # $ANTLR end "type"


    # $ANTLR start "function_block_body"
    # FCL.g:158:1: function_block_body : ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )* ;
    def function_block_body(self, ):

        try:
            try:
                # FCL.g:159:2: ( ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )* )
                # FCL.g:160:4: ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )*
                pass 
                # FCL.g:160:4: ( fuzzify_block )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 24) :
                        alt8 = 1


                    if alt8 == 1:
                        # FCL.g:160:4: fuzzify_block
                        pass 
                        self._state.following.append(self.FOLLOW_fuzzify_block_in_function_block_body263)
                        self.fuzzify_block()

                        self._state.following.pop()


                    else:
                        break #loop8


                # FCL.g:161:4: ( defuzzify_block )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 26) :
                        alt9 = 1


                    if alt9 == 1:
                        # FCL.g:161:4: defuzzify_block
                        pass 
                        self._state.following.append(self.FOLLOW_defuzzify_block_in_function_block_body269)
                        self.defuzzify_block()

                        self._state.following.pop()


                    else:
                        break #loop9


                # FCL.g:162:7: ( rule_block )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 28) :
                        alt10 = 1


                    if alt10 == 1:
                        # FCL.g:162:7: rule_block
                        pass 
                        self._state.following.append(self.FOLLOW_rule_block_in_function_block_body278)
                        self.rule_block()

                        self._state.following.pop()


                    else:
                        break #loop10


                # FCL.g:163:4: ( option_block )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 30) :
                        alt11 = 1


                    if alt11 == 1:
                        # FCL.g:163:4: option_block
                        pass 
                        self._state.following.append(self.FOLLOW_option_block_in_function_block_body284)
                        self.option_block()

                        self._state.following.pop()


                    else:
                        break #loop11






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "function_block_body"


    # $ANTLR start "fuzzify_block"
    # FCL.g:166:1: fuzzify_block : 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY' ;
    def fuzzify_block(self, ):

        variable_name7 = None


        try:
            try:
                # FCL.g:167:2: ( 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY' )
                # FCL.g:168:4: 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY'
                pass 
                self.match(self.input, 24, self.FOLLOW_24_in_fuzzify_block301)
                self._state.following.append(self.FOLLOW_variable_name_in_fuzzify_block307)
                variable_name7 = self.variable_name()

                self._state.following.pop()
                # FCL.g:170:4: ( linguistic_term[$variable_name.text] )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 32) :
                        alt12 = 1


                    if alt12 == 1:
                        # FCL.g:170:4: linguistic_term[$variable_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_linguistic_term_in_fuzzify_block312)
                        self.linguistic_term(((variable_name7 is not None) and [self.input.toString(variable_name7.start,variable_name7.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop12


                self.match(self.input, 25, self.FOLLOW_25_in_fuzzify_block319)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "fuzzify_block"


    # $ANTLR start "defuzzify_block"
    # FCL.g:174:1: defuzzify_block : 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY' ;
    def defuzzify_block(self, ):

        f_variable_name8 = None


        try:
            try:
                # FCL.g:175:2: ( 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY' )
                # FCL.g:176:4: 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY'
                pass 
                self.match(self.input, 26, self.FOLLOW_26_in_defuzzify_block335)
                self._state.following.append(self.FOLLOW_f_variable_name_in_defuzzify_block341)
                f_variable_name8 = self.f_variable_name()

                self._state.following.pop()
                # FCL.g:178:4: ( linguistic_term[$f_variable_name.text] )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 32) :
                        alt13 = 1


                    if alt13 == 1:
                        # FCL.g:178:4: linguistic_term[$f_variable_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_linguistic_term_in_defuzzify_block346)
                        self.linguistic_term(((f_variable_name8 is not None) and [self.input.toString(f_variable_name8.start,f_variable_name8.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop13


                self._state.following.append(self.FOLLOW_accumulation_method_in_defuzzify_block353)
                self.accumulation_method()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_defuzzification_method_in_defuzzify_block358)
                self.defuzzification_method(((f_variable_name8 is not None) and [self.input.toString(f_variable_name8.start,f_variable_name8.stop)] or [None])[0])

                self._state.following.pop()
                # FCL.g:181:4: ( default_value[$f_variable_name.text] )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 38) :
                    alt14 = 1
                if alt14 == 1:
                    # FCL.g:181:4: default_value[$f_variable_name.text]
                    pass 
                    self._state.following.append(self.FOLLOW_default_value_in_defuzzify_block364)
                    self.default_value(((f_variable_name8 is not None) and [self.input.toString(f_variable_name8.start,f_variable_name8.stop)] or [None])[0])

                    self._state.following.pop()



                # FCL.g:182:4: ( range )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 40) :
                    alt15 = 1
                if alt15 == 1:
                    # FCL.g:182:4: range
                    pass 
                    self._state.following.append(self.FOLLOW_range_in_defuzzify_block371)
                    self.range()

                    self._state.following.pop()



                self.match(self.input, 27, self.FOLLOW_27_in_defuzzify_block377)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "defuzzify_block"


    # $ANTLR start "rule_block"
    # FCL.g:186:1: rule_block : 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK' ;
    def rule_block(self, ):

        rule_block_name9 = None


        try:
            try:
                # FCL.g:187:2: ( 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK' )
                # FCL.g:188:4: 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK'
                pass 
                self.match(self.input, 28, self.FOLLOW_28_in_rule_block394)
                self._state.following.append(self.FOLLOW_rule_block_name_in_rule_block401)
                rule_block_name9 = self.rule_block_name()

                self._state.following.pop()
                # FCL.g:190:5: ( operator_definition )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((OR_ <= LA16_0 <= AND_)) :
                        alt16 = 1


                    if alt16 == 1:
                        # FCL.g:190:5: operator_definition
                        pass 
                        self._state.following.append(self.FOLLOW_operator_definition_in_rule_block407)
                        self.operator_definition()

                        self._state.following.pop()


                    else:
                        break #loop16


                # FCL.g:191:5: ( activation_method )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == 50) :
                    alt17 = 1
                if alt17 == 1:
                    # FCL.g:191:5: activation_method
                    pass 
                    self._state.following.append(self.FOLLOW_activation_method_in_rule_block414)
                    self.activation_method()

                    self._state.following.pop()



                # FCL.g:192:5: ( rule[$rule_block_name.text] )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == 56) :
                        alt18 = 1


                    if alt18 == 1:
                        # FCL.g:192:5: rule[$rule_block_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_rule_in_rule_block421)
                        self.rule(((rule_block_name9 is not None) and [self.input.toString(rule_block_name9.start,rule_block_name9.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop18


                self.match(self.input, 29, self.FOLLOW_29_in_rule_block428)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "rule_block"


    # $ANTLR start "option_block"
    # FCL.g:196:1: option_block : 'OPTION' 'END_OPTION' ;
    def option_block(self, ):

        try:
            try:
                # FCL.g:196:14: ( 'OPTION' 'END_OPTION' )
                # FCL.g:196:16: 'OPTION' 'END_OPTION'
                pass 
                self.match(self.input, 30, self.FOLLOW_30_in_option_block437)
                self.match(self.input, 31, self.FOLLOW_31_in_option_block441)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "option_block"


    # $ANTLR start "linguistic_term"
    # FCL.g:201:1: linguistic_term[var_name] : 'TERM' term_name ':=' membership_function ';' ;
    def linguistic_term(self, var_name):

        term_name10 = None

        membership_function11 = None


        try:
            try:
                # FCL.g:202:2: ( 'TERM' term_name ':=' membership_function ';' )
                # FCL.g:203:2: 'TERM' term_name ':=' membership_function ';'
                pass 
                self.match(self.input, 32, self.FOLLOW_32_in_linguistic_term455)
                self._state.following.append(self.FOLLOW_term_name_in_linguistic_term457)
                term_name10 = self.term_name()

                self._state.following.pop()
                self.match(self.input, 33, self.FOLLOW_33_in_linguistic_term459)
                self._state.following.append(self.FOLLOW_membership_function_in_linguistic_term461)
                membership_function11 = self.membership_function()

                self._state.following.pop()
                self.match(self.input, 20, self.FOLLOW_20_in_linguistic_term463)
                #action start
                 
                self.System.variables[var_name].adjectives[((term_name10 is not None) and [self.input.toString(term_name10.start,term_name10.stop)] or [None])[0]]=fuzzy.Adjective.Adjective(membership_function11);

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "linguistic_term"


    # $ANTLR start "membership_function"
    # FCL.g:210:1: membership_function returns [set] : ( singleton | points );
    def membership_function(self, ):

        set = None

        singleton12 = None

        points13 = None


        try:
            try:
                # FCL.g:211:2: ( singleton | points )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == Identifier or (Integer_literal <= LA19_0 <= Real_literal)) :
                    alt19 = 1
                elif (LA19_0 == 20 or LA19_0 == 34) :
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # FCL.g:212:3: singleton
                    pass 
                    self._state.following.append(self.FOLLOW_singleton_in_membership_function484)
                    singleton12 = self.singleton()

                    self._state.following.pop()
                    #action start
                    set =  singleton12
                    #action end


                elif alt19 == 2:
                    # FCL.g:214:3: points
                    pass 
                    self._state.following.append(self.FOLLOW_points_in_membership_function495)
                    points13 = self.points()

                    self._state.following.pop()
                    #action start
                    set =  points13
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "membership_function"


    # $ANTLR start "singleton"
    # FCL.g:217:1: singleton returns [set] : ( numeric_literal | variable_name );
    def singleton(self, ):

        set = None

        numeric_literal14 = None


        try:
            try:
                # FCL.g:218:2: ( numeric_literal | variable_name )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((Integer_literal <= LA20_0 <= Real_literal)) :
                    alt20 = 1
                elif (LA20_0 == Identifier) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # FCL.g:219:3: numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_singleton516)
                    numeric_literal14 = self.numeric_literal()

                    self._state.following.pop()
                    #action start
                    set =  fuzzy.set.Singleton.Singleton(float(((numeric_literal14 is not None) and [self.input.toString(numeric_literal14.start,numeric_literal14.stop)] or [None])[0]))
                    #action end


                elif alt20 == 2:
                    # FCL.g:221:3: variable_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_singleton527)
                    self.variable_name()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "singleton"


    # $ANTLR start "points"
    # FCL.g:224:1: points returns [set] : ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )* ;
    def points(self, ):

        set = None

        x = None

        y = None


               
        p=[]

        try:
            try:
                # FCL.g:228:2: ( ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )* )
                # FCL.g:229:3: ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )*
                pass 
                # FCL.g:229:3: ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == 34) :
                        alt22 = 1


                    if alt22 == 1:
                        # FCL.g:230:4: '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')'
                        pass 
                        self.match(self.input, 34, self.FOLLOW_34_in_points554)
                        # FCL.g:231:4: (x= numeric_literal | variable_name )
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if ((Integer_literal <= LA21_0 <= Real_literal)) :
                            alt21 = 1
                        elif (LA21_0 == Identifier) :
                            alt21 = 2
                        else:
                            nvae = NoViableAltException("", 21, 0, self.input)

                            raise nvae

                        if alt21 == 1:
                            # FCL.g:231:5: x= numeric_literal
                            pass 
                            self._state.following.append(self.FOLLOW_numeric_literal_in_points563)
                            x = self.numeric_literal()

                            self._state.following.pop()


                        elif alt21 == 2:
                            # FCL.g:231:25: variable_name
                            pass 
                            self._state.following.append(self.FOLLOW_variable_name_in_points567)
                            self.variable_name()

                            self._state.following.pop()



                        self.match(self.input, 35, self.FOLLOW_35_in_points574)
                        self._state.following.append(self.FOLLOW_numeric_literal_in_points582)
                        y = self.numeric_literal()

                        self._state.following.pop()
                        self.match(self.input, 36, self.FOLLOW_36_in_points588)
                        #action start
                        p.append((float(((x is not None) and [self.input.toString(x.start,x.stop)] or [None])[0]),float(((y is not None) and [self.input.toString(y.start,y.stop)] or [None])[0])));
                        #action end


                    else:
                        break #loop22


                #action start
                set =  fuzzy.set.Polygon.Polygon(p)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "points"


    # $ANTLR start "defuzzification_method"
    # FCL.g:242:1: defuzzification_method[var_name] : 'METHOD' ':' Identifier ';' ;
    def defuzzification_method(self, var_name):

        Identifier15 = None

        try:
            try:
                # FCL.g:242:35: ( 'METHOD' ':' Identifier ';' )
                # FCL.g:243:2: 'METHOD' ':' Identifier ';'
                pass 
                self.match(self.input, 37, self.FOLLOW_37_in_defuzzification_method623)
                self.match(self.input, 18, self.FOLLOW_18_in_defuzzification_method625)
                Identifier15=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_defuzzification_method629)
                #action start
                self.System.variables[var_name].defuzzify = getDefuzzificationMethod(Identifier15.text);
                #action end
                self.match(self.input, 20, self.FOLLOW_20_in_defuzzification_method634)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "defuzzification_method"


    # $ANTLR start "default_value"
    # FCL.g:249:1: default_value[var_name] : 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';' ;
    def default_value(self, var_name):

        numeric_literal16 = None


        try:
            try:
                # FCL.g:249:26: ( 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';' )
                # FCL.g:250:2: 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';'
                pass 
                self.match(self.input, 38, self.FOLLOW_38_in_default_value649)
                self.match(self.input, 33, self.FOLLOW_33_in_default_value651)
                # FCL.g:251:2: ( numeric_literal | 'NC' )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if ((Integer_literal <= LA23_0 <= Real_literal)) :
                    alt23 = 1
                elif (LA23_0 == 39) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # FCL.g:252:3: numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_default_value659)
                    numeric_literal16 = self.numeric_literal()

                    self._state.following.pop()
                    #action start
                    self.System.variables[var_name].defuzzify.failsafe = float(((numeric_literal16 is not None) and [self.input.toString(numeric_literal16.start,numeric_literal16.stop)] or [None])[0]);
                    #action end


                elif alt23 == 2:
                    # FCL.g:254:3: 'NC'
                    pass 
                    self.match(self.input, 39, self.FOLLOW_39_in_default_value669)
                    #action start
                    self.System.variables[var_name].defuzzify.failsafe = None;
                    #action end



                self.match(self.input, 20, self.FOLLOW_20_in_default_value678)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "default_value"


    # $ANTLR start "range"
    # FCL.g:259:1: range : 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';' ;
    def range(self, ):

        try:
            try:
                # FCL.g:259:7: ( 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';' )
                # FCL.g:259:9: 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';'
                pass 
                self.match(self.input, 40, self.FOLLOW_40_in_range688)
                self.match(self.input, 33, self.FOLLOW_33_in_range690)
                self.match(self.input, 34, self.FOLLOW_34_in_range692)
                self._state.following.append(self.FOLLOW_numeric_literal_in_range694)
                self.numeric_literal()

                self._state.following.pop()
                self.match(self.input, 41, self.FOLLOW_41_in_range696)
                self._state.following.append(self.FOLLOW_numeric_literal_in_range698)
                self.numeric_literal()

                self._state.following.pop()
                self.match(self.input, 36, self.FOLLOW_36_in_range700)
                self.match(self.input, 20, self.FOLLOW_20_in_range702)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "range"


    # $ANTLR start "operator_name_any"
    # FCL.g:262:1: operator_name_any returns [op] : i1= Identifier ( '[' param= numeric_literal ']' )? ;
    def operator_name_any(self, ):

        op = None

        i1 = None
        param = None


        try:
            try:
                # FCL.g:263:2: (i1= Identifier ( '[' param= numeric_literal ']' )? )
                # FCL.g:264:2: i1= Identifier ( '[' param= numeric_literal ']' )?
                pass 
                i1=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_operator_name_any721)
                # FCL.g:264:16: ( '[' param= numeric_literal ']' )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == 42) :
                    alt24 = 1
                if alt24 == 1:
                    # FCL.g:264:17: '[' param= numeric_literal ']'
                    pass 
                    self.match(self.input, 42, self.FOLLOW_42_in_operator_name_any724)
                    self._state.following.append(self.FOLLOW_numeric_literal_in_operator_name_any728)
                    param = self.numeric_literal()

                    self._state.following.pop()
                    self.match(self.input, 43, self.FOLLOW_43_in_operator_name_any730)



                #action start
                                                                 
                if ((param is not None) and [self.input.toString(param.start,param.stop)] or [None])[0] is not None:
                	p = float(((param is not None) and [self.input.toString(param.start,param.stop)] or [None])[0])
                else:
                	p = None
                op =  getNorm(i1.text,p)
                	
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "operator_name_any"


    # $ANTLR start "operator_name_AND"
    # FCL.g:274:1: operator_name_AND returns [op] : ( ( 'MIN' ) | ( 'PROD' ) | ( 'BDIF' ) | (norm= operator_name_any ) );
    def operator_name_AND(self, ):

        op = None

        norm = None


        try:
            try:
                # FCL.g:275:2: ( ( 'MIN' ) | ( 'PROD' ) | ( 'BDIF' ) | (norm= operator_name_any ) )
                alt25 = 4
                LA25 = self.input.LA(1)
                if LA25 == 44:
                    alt25 = 1
                elif LA25 == 45:
                    alt25 = 2
                elif LA25 == 46:
                    alt25 = 3
                elif LA25 == Identifier:
                    alt25 = 4
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # FCL.g:275:4: ( 'MIN' )
                    pass 
                    # FCL.g:275:4: ( 'MIN' )
                    # FCL.g:275:5: 'MIN'
                    pass 
                    self.match(self.input, 44, self.FOLLOW_44_in_operator_name_AND751)
                    #action start
                    op = getNorm("Min")
                    #action end





                elif alt25 == 2:
                    # FCL.g:276:5: ( 'PROD' )
                    pass 
                    # FCL.g:276:5: ( 'PROD' )
                    # FCL.g:276:6: 'PROD'
                    pass 
                    self.match(self.input, 45, self.FOLLOW_45_in_operator_name_AND761)
                    #action start
                    op = getNorm("AlgebraicProduct")
                    #action end





                elif alt25 == 3:
                    # FCL.g:277:5: ( 'BDIF' )
                    pass 
                    # FCL.g:277:5: ( 'BDIF' )
                    # FCL.g:277:6: 'BDIF'
                    pass 
                    self.match(self.input, 46, self.FOLLOW_46_in_operator_name_AND772)
                    #action start
                    op = getNorm("BoundedDifference")
                    #action end





                elif alt25 == 4:
                    # FCL.g:278:4: (norm= operator_name_any )
                    pass 
                    # FCL.g:278:4: (norm= operator_name_any )
                    # FCL.g:278:5: norm= operator_name_any
                    pass 
                    self._state.following.append(self.FOLLOW_operator_name_any_in_operator_name_AND784)
                    norm = self.operator_name_any()

                    self._state.following.pop()
                    #action start
                    op = norm
                    #action end






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "operator_name_AND"


    # $ANTLR start "operator_name_OR"
    # FCL.g:281:1: operator_name_OR returns [op] : ( ( 'MAX' ) | ( 'ASUM' ) | ( 'BSUM' ) | (norm= operator_name_any ) );
    def operator_name_OR(self, ):

        op = None

        norm = None


        try:
            try:
                # FCL.g:282:2: ( ( 'MAX' ) | ( 'ASUM' ) | ( 'BSUM' ) | (norm= operator_name_any ) )
                alt26 = 4
                LA26 = self.input.LA(1)
                if LA26 == 47:
                    alt26 = 1
                elif LA26 == 48:
                    alt26 = 2
                elif LA26 == 49:
                    alt26 = 3
                elif LA26 == Identifier:
                    alt26 = 4
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # FCL.g:282:4: ( 'MAX' )
                    pass 
                    # FCL.g:282:4: ( 'MAX' )
                    # FCL.g:282:5: 'MAX'
                    pass 
                    self.match(self.input, 47, self.FOLLOW_47_in_operator_name_OR803)
                    #action start
                    op = getNorm("Max")
                    #action end





                elif alt26 == 2:
                    # FCL.g:283:5: ( 'ASUM' )
                    pass 
                    # FCL.g:283:5: ( 'ASUM' )
                    # FCL.g:283:6: 'ASUM'
                    pass 
                    self.match(self.input, 48, self.FOLLOW_48_in_operator_name_OR813)
                    #action start
                    op = getNorm("AlgebraicSum")
                    #action end





                elif alt26 == 3:
                    # FCL.g:284:5: ( 'BSUM' )
                    pass 
                    # FCL.g:284:5: ( 'BSUM' )
                    # FCL.g:284:6: 'BSUM'
                    pass 
                    self.match(self.input, 49, self.FOLLOW_49_in_operator_name_OR824)
                    #action start
                    op = getNorm("BoundedSum")
                    #action end





                elif alt26 == 4:
                    # FCL.g:285:4: (norm= operator_name_any )
                    pass 
                    # FCL.g:285:4: (norm= operator_name_any )
                    # FCL.g:285:5: norm= operator_name_any
                    pass 
                    self._state.following.append(self.FOLLOW_operator_name_any_in_operator_name_OR836)
                    norm = self.operator_name_any()

                    self._state.following.pop()
                    #action start
                    op = norm
                    #action end






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "operator_name_OR"


    # $ANTLR start "operator_definition"
    # FCL.g:291:1: operator_definition : ( (or_name= OR_ ':' or_op= operator_name_OR ) | (and_name= AND_ ':' and_op= operator_name_AND ) ) ';' ;
    def operator_definition(self, ):

        or_name = None
        and_name = None
        or_op = None

        and_op = None


        try:
            try:
                # FCL.g:291:21: ( ( (or_name= OR_ ':' or_op= operator_name_OR ) | (and_name= AND_ ':' and_op= operator_name_AND ) ) ';' )
                # FCL.g:292:1: ( (or_name= OR_ ':' or_op= operator_name_OR ) | (and_name= AND_ ':' and_op= operator_name_AND ) ) ';'
                pass 
                # FCL.g:292:1: ( (or_name= OR_ ':' or_op= operator_name_OR ) | (and_name= AND_ ':' and_op= operator_name_AND ) )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == OR_) :
                    alt27 = 1
                elif (LA27_0 == AND_) :
                    alt27 = 2
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # FCL.g:293:1: (or_name= OR_ ':' or_op= operator_name_OR )
                    pass 
                    # FCL.g:293:1: (or_name= OR_ ':' or_op= operator_name_OR )
                    # FCL.g:293:2: or_name= OR_ ':' or_op= operator_name_OR
                    pass 
                    or_name=self.match(self.input, OR_, self.FOLLOW_OR__in_operator_definition878)
                    self.match(self.input, 18, self.FOLLOW_18_in_operator_definition880)
                    self._state.following.append(self.FOLLOW_operator_name_OR_in_operator_definition884)
                    or_op = self.operator_name_OR()

                    self._state.following.pop()
                    #action start
                    defineOperator(or_name.text,or_op);
                    #action end





                elif alt27 == 2:
                    # FCL.g:295:1: (and_name= AND_ ':' and_op= operator_name_AND )
                    pass 
                    # FCL.g:295:1: (and_name= AND_ ':' and_op= operator_name_AND )
                    # FCL.g:295:2: and_name= AND_ ':' and_op= operator_name_AND
                    pass 
                    and_name=self.match(self.input, AND_, self.FOLLOW_AND__in_operator_definition895)
                    self.match(self.input, 18, self.FOLLOW_18_in_operator_definition897)
                    self._state.following.append(self.FOLLOW_operator_name_AND_in_operator_definition901)
                    and_op = self.operator_name_AND()

                    self._state.following.pop()
                    #action start
                    defineOperator(and_name.text,and_op);
                    #action end






                self.match(self.input, 20, self.FOLLOW_20_in_operator_definition910)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "operator_definition"


    # $ANTLR start "activation_method"
    # FCL.g:300:1: activation_method : 'ACT' ':' ( 'PROD' | 'MIN' ) ';' ;
    def activation_method(self, ):

        try:
            try:
                # FCL.g:300:19: ( 'ACT' ':' ( 'PROD' | 'MIN' ) ';' )
                # FCL.g:300:21: 'ACT' ':' ( 'PROD' | 'MIN' ) ';'
                pass 
                self.match(self.input, 50, self.FOLLOW_50_in_activation_method919)
                self.match(self.input, 18, self.FOLLOW_18_in_activation_method921)
                if (44 <= self.input.LA(1) <= 45):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self.match(self.input, 20, self.FOLLOW_20_in_activation_method931)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "activation_method"


    # $ANTLR start "accumulation_method"
    # FCL.g:302:1: accumulation_method : 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';' ;
    def accumulation_method(self, ):

        try:
            try:
                # FCL.g:302:21: ( 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';' )
                # FCL.g:302:23: 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';'
                pass 
                self.match(self.input, 51, self.FOLLOW_51_in_accumulation_method939)
                self.match(self.input, 18, self.FOLLOW_18_in_accumulation_method941)
                if self.input.LA(1) == 47 or self.input.LA(1) == 49 or self.input.LA(1) == 52:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self.match(self.input, 20, self.FOLLOW_20_in_accumulation_method955)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "accumulation_method"


    # $ANTLR start "condition"
    # FCL.g:307:1: condition returns [input] : (s1= subcondition ) ( (op= ( AND_ | OR_ ) s2= subcondition ) )* ;
    def condition(self, ):

        input = None

        op = None
        s1 = None

        s2 = None


              
        op_name = None;

        try:
            try:
                # FCL.g:311:2: ( (s1= subcondition ) ( (op= ( AND_ | OR_ ) s2= subcondition ) )* )
                # FCL.g:312:2: (s1= subcondition ) ( (op= ( AND_ | OR_ ) s2= subcondition ) )*
                pass 
                # FCL.g:312:2: (s1= subcondition )
                # FCL.g:313:3: s1= subcondition
                pass 
                self._state.following.append(self.FOLLOW_subcondition_in_condition983)
                s1 = self.subcondition()

                self._state.following.pop()
                #action start
                input = s1
                #action end



                # FCL.g:317:2: ( (op= ( AND_ | OR_ ) s2= subcondition ) )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if ((OR_ <= LA28_0 <= AND_)) :
                        alt28 = 1


                    if alt28 == 1:
                        # FCL.g:318:3: (op= ( AND_ | OR_ ) s2= subcondition )
                        pass 
                        # FCL.g:318:3: (op= ( AND_ | OR_ ) s2= subcondition )
                        # FCL.g:319:4: op= ( AND_ | OR_ ) s2= subcondition
                        pass 
                        op = self.input.LT(1)
                        if (OR_ <= self.input.LA(1) <= AND_):
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        #action start
                            
                        if op_name is not None and op_name != op.text:
                        	raise Exception("Don't mix different operations in an expression.")
                        else:
                        	op_name = op.text
                        			
                        #action end
                        self._state.following.append(self.FOLLOW_subcondition_in_condition1022)
                        s2 = self.subcondition()

                        self._state.following.pop()
                        #action start
                            
                        input =  fuzzy.operator.Compound.Compound(getOperator(op.text),input,s2)
                        			
                        #action end





                    else:
                        break #loop28






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "condition"


    # $ANTLR start "subcondition"
    # FCL.g:337:1: subcondition returns [input] : ( ( 'NOT' '(' condition ')' ) | ( subcondition2 ) );
    def subcondition(self, ):

        input = None

        condition17 = None

        subcondition218 = None


        try:
            try:
                # FCL.g:338:2: ( ( 'NOT' '(' condition ')' ) | ( subcondition2 ) )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == 53) :
                    alt29 = 1
                elif (LA29_0 == Identifier or LA29_0 == 34) :
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # FCL.g:338:4: ( 'NOT' '(' condition ')' )
                    pass 
                    # FCL.g:338:4: ( 'NOT' '(' condition ')' )
                    # FCL.g:338:5: 'NOT' '(' condition ')'
                    pass 
                    self.match(self.input, 53, self.FOLLOW_53_in_subcondition1055)
                    self.match(self.input, 34, self.FOLLOW_34_in_subcondition1057)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition1059)
                    condition17 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 36, self.FOLLOW_36_in_subcondition1061)
                    #action start
                    input =  fuzzy.operator.Not.Not(condition17)
                    #action end





                elif alt29 == 2:
                    # FCL.g:339:4: ( subcondition2 )
                    pass 
                    # FCL.g:339:4: ( subcondition2 )
                    # FCL.g:339:6: subcondition2
                    pass 
                    self._state.following.append(self.FOLLOW_subcondition2_in_subcondition1072)
                    subcondition218 = self.subcondition2()

                    self._state.following.pop()
                    #action start
                    input =  subcondition218
                    #action end






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "subcondition"


    # $ANTLR start "subcondition2"
    # FCL.g:346:1: subcondition2 returns [input] : ( ( '(' c1= condition ')' ) | ( variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name ) | (norm= operator_name_any '(' c4= condition ',' c5= condition ')' ) );
    def subcondition2(self, ):

        input = None

        x = None
        c1 = None

        norm = None

        c4 = None

        c5 = None

        variable_name19 = None

        term_name20 = None


        try:
            try:
                # FCL.g:347:2: ( ( '(' c1= condition ')' ) | ( variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name ) | (norm= operator_name_any '(' c4= condition ',' c5= condition ')' ) )
                alt32 = 3
                LA32_0 = self.input.LA(1)

                if (LA32_0 == 34) :
                    alt32 = 1
                elif (LA32_0 == Identifier) :
                    LA32_2 = self.input.LA(2)

                    if (LA32_2 == 34 or LA32_2 == 42) :
                        alt32 = 3
                    elif ((54 <= LA32_2 <= 55)) :
                        alt32 = 2
                    else:
                        nvae = NoViableAltException("", 32, 2, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # FCL.g:348:2: ( '(' c1= condition ')' )
                    pass 
                    # FCL.g:348:2: ( '(' c1= condition ')' )
                    # FCL.g:348:3: '(' c1= condition ')'
                    pass 
                    self.match(self.input, 34, self.FOLLOW_34_in_subcondition21097)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition21101)
                    c1 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 36, self.FOLLOW_36_in_subcondition21103)
                    #action start
                       
                    input =  c1
                    		
                    #action end





                elif alt32 == 2:
                    # FCL.g:354:2: ( variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name )
                    pass 
                    # FCL.g:354:2: ( variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name )
                    # FCL.g:354:4: variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_subcondition21121)
                    variable_name19 = self.variable_name()

                    self._state.following.pop()
                    # FCL.g:354:18: ( 'IS' (x= 'NOT' )? | '.' )
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == 54) :
                        alt31 = 1
                    elif (LA31_0 == 55) :
                        alt31 = 2
                    else:
                        nvae = NoViableAltException("", 31, 0, self.input)

                        raise nvae

                    if alt31 == 1:
                        # FCL.g:354:19: 'IS' (x= 'NOT' )?
                        pass 
                        self.match(self.input, 54, self.FOLLOW_54_in_subcondition21124)
                        # FCL.g:354:25: (x= 'NOT' )?
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == 53) :
                            alt30 = 1
                        if alt30 == 1:
                            # FCL.g:354:25: x= 'NOT'
                            pass 
                            x=self.match(self.input, 53, self.FOLLOW_53_in_subcondition21128)





                    elif alt31 == 2:
                        # FCL.g:354:35: '.'
                        pass 
                        self.match(self.input, 55, self.FOLLOW_55_in_subcondition21133)



                    self._state.following.append(self.FOLLOW_term_name_in_subcondition21137)
                    term_name20 = self.term_name()

                    self._state.following.pop()
                    #action start
                       
                    input = fuzzy.operator.Input.Input(self.System.variables[((variable_name19 is not None) and [self.input.toString(variable_name19.start,variable_name19.stop)] or [None])[0]].adjectives[((term_name20 is not None) and [self.input.toString(term_name20.start,term_name20.stop)] or [None])[0]])
                    if x is not None:
                    	input = fuzzy.operator.Not.Not(input)
                    		
                    #action end





                elif alt32 == 3:
                    # FCL.g:362:2: (norm= operator_name_any '(' c4= condition ',' c5= condition ')' )
                    pass 
                    # FCL.g:362:2: (norm= operator_name_any '(' c4= condition ',' c5= condition ')' )
                    # FCL.g:362:3: norm= operator_name_any '(' c4= condition ',' c5= condition ')'
                    pass 
                    self._state.following.append(self.FOLLOW_operator_name_any_in_subcondition21155)
                    norm = self.operator_name_any()

                    self._state.following.pop()
                    self.match(self.input, 34, self.FOLLOW_34_in_subcondition21157)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition21161)
                    c4 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 35, self.FOLLOW_35_in_subcondition21163)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition21167)
                    c5 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 36, self.FOLLOW_36_in_subcondition21169)
                    #action start
                       
                    input =  fuzzy.operator.Compound.Compound(norm,c4,c5)
                    		
                    #action end






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "subcondition2"


    # $ANTLR start "conclusion"
    # FCL.g:371:1: conclusion returns [adjs] : ( (c1= conclusion2 ) ( ',' c2= conclusion2 )* ) ;
    def conclusion(self, ):

        adjs = None

        c1 = None

        c2 = None


              
        _adjs=[]

        try:
            try:
                # FCL.g:375:2: ( ( (c1= conclusion2 ) ( ',' c2= conclusion2 )* ) )
                # FCL.g:375:4: ( (c1= conclusion2 ) ( ',' c2= conclusion2 )* )
                pass 
                # FCL.g:375:4: ( (c1= conclusion2 ) ( ',' c2= conclusion2 )* )
                # FCL.g:376:3: (c1= conclusion2 ) ( ',' c2= conclusion2 )*
                pass 
                # FCL.g:376:3: (c1= conclusion2 )
                # FCL.g:376:9: c1= conclusion2
                pass 
                self._state.following.append(self.FOLLOW_conclusion2_in_conclusion1211)
                c1 = self.conclusion2()

                self._state.following.pop()
                #action start
                _adjs.append(c1);
                #action end



                # FCL.g:377:3: ( ',' c2= conclusion2 )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == 35) :
                        alt33 = 1


                    if alt33 == 1:
                        # FCL.g:377:6: ',' c2= conclusion2
                        pass 
                        self.match(self.input, 35, self.FOLLOW_35_in_conclusion1223)
                        self._state.following.append(self.FOLLOW_conclusion2_in_conclusion1227)
                        c2 = self.conclusion2()

                        self._state.following.pop()
                        #action start
                        _adjs.append(c2);
                        #action end


                    else:
                        break #loop33





                #action start
                adjs =  _adjs 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adjs

    # $ANTLR end "conclusion"


    # $ANTLR start "conclusion2"
    # FCL.g:381:1: conclusion2 returns [adj] : ( ( '(' c2= conclusion3 ')' ) | (c1= conclusion3 ) );
    def conclusion2(self, ):

        adj = None

        c2 = None

        c1 = None


        try:
            try:
                # FCL.g:382:2: ( ( '(' c2= conclusion3 ')' ) | (c1= conclusion3 ) )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == 34) :
                    alt34 = 1
                elif (LA34_0 == Identifier) :
                    alt34 = 2
                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # FCL.g:383:2: ( '(' c2= conclusion3 ')' )
                    pass 
                    # FCL.g:383:2: ( '(' c2= conclusion3 ')' )
                    # FCL.g:383:4: '(' c2= conclusion3 ')'
                    pass 
                    self.match(self.input, 34, self.FOLLOW_34_in_conclusion21258)
                    self._state.following.append(self.FOLLOW_conclusion3_in_conclusion21262)
                    c2 = self.conclusion3()

                    self._state.following.pop()
                    self.match(self.input, 36, self.FOLLOW_36_in_conclusion21265)
                    #action start
                    adj = c2
                    #action end





                elif alt34 == 2:
                    # FCL.g:385:2: (c1= conclusion3 )
                    pass 
                    # FCL.g:385:2: (c1= conclusion3 )
                    # FCL.g:385:8: c1= conclusion3
                    pass 
                    self._state.following.append(self.FOLLOW_conclusion3_in_conclusion21284)
                    c1 = self.conclusion3()

                    self._state.following.pop()
                    #action start
                    adj = c1
                    #action end






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adj

    # $ANTLR end "conclusion2"


    # $ANTLR start "conclusion3"
    # FCL.g:388:1: conclusion3 returns [adj] : ( (v2= variable_name 'IS' t2= term_name ) ) ;
    def conclusion3(self, ):

        adj = None

        v2 = None

        t2 = None


        try:
            try:
                # FCL.g:389:2: ( ( (v2= variable_name 'IS' t2= term_name ) ) )
                # FCL.g:390:2: ( (v2= variable_name 'IS' t2= term_name ) )
                pass 
                # FCL.g:390:2: ( (v2= variable_name 'IS' t2= term_name ) )
                # FCL.g:393:2: (v2= variable_name 'IS' t2= term_name )
                pass 
                # FCL.g:393:2: (v2= variable_name 'IS' t2= term_name )
                # FCL.g:393:3: v2= variable_name 'IS' t2= term_name
                pass 
                self._state.following.append(self.FOLLOW_variable_name_in_conclusion31318)
                v2 = self.variable_name()

                self._state.following.pop()
                self.match(self.input, 54, self.FOLLOW_54_in_conclusion31320)
                self._state.following.append(self.FOLLOW_term_name_in_conclusion31324)
                t2 = self.term_name()

                self._state.following.pop()
                #action start
                adj = self.System.variables[((v2 is not None) and [self.input.toString(v2.start,v2.stop)] or [None])[0]].adjectives[((t2 is not None) and [self.input.toString(t2.start,t2.stop)] or [None])[0]]
                #action end










            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adj

    # $ANTLR end "conclusion3"


    # $ANTLR start "rule"
    # FCL.g:398:1: rule[block_name] : 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';' ;
    def rule(self, block_name):

        Integer_literal24 = None
        weighting_factor21 = None

        condition22 = None

        conclusion23 = None


              
        certainty = 1.0

        try:
            try:
                # FCL.g:401:3: ( 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';' )
                # FCL.g:401:5: 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';'
                pass 
                self.match(self.input, 56, self.FOLLOW_56_in_rule1347)
                Integer_literal24=self.match(self.input, Integer_literal, self.FOLLOW_Integer_literal_in_rule1349)
                self.match(self.input, 18, self.FOLLOW_18_in_rule1351)
                self.match(self.input, 57, self.FOLLOW_57_in_rule1353)
                self._state.following.append(self.FOLLOW_condition_in_rule1355)
                condition22 = self.condition()

                self._state.following.pop()
                self.match(self.input, 58, self.FOLLOW_58_in_rule1357)
                self._state.following.append(self.FOLLOW_conclusion_in_rule1359)
                conclusion23 = self.conclusion()

                self._state.following.pop()
                # FCL.g:401:65: ( 'WITH' weighting_factor )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == 59) :
                    alt35 = 1
                if alt35 == 1:
                    # FCL.g:401:66: 'WITH' weighting_factor
                    pass 
                    self.match(self.input, 59, self.FOLLOW_59_in_rule1362)
                    self._state.following.append(self.FOLLOW_weighting_factor_in_rule1364)
                    weighting_factor21 = self.weighting_factor()

                    self._state.following.pop()
                    #action start
                    certainty = float(((weighting_factor21 is not None) and [self.input.toString(weighting_factor21.start,weighting_factor21.stop)] or [None])[0]);
                    #action end



                self.match(self.input, 20, self.FOLLOW_20_in_rule1370)
                #action start
                 
                input = condition22
                adjective = conclusion23
                self.System.rules[block_name+'.'+Integer_literal24.text] = fuzzy.Rule.Rule(adjective,input,certainty=certainty)

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "rule"

    class weighting_factor_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "weighting_factor"
    # FCL.g:409:1: weighting_factor : numeric_literal ;
    def weighting_factor(self, ):

        retval = self.weighting_factor_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:409:18: ( numeric_literal )
                # FCL.g:412:2: numeric_literal
                pass 
                self._state.following.append(self.FOLLOW_numeric_literal_in_weighting_factor1385)
                self.numeric_literal()

                self._state.following.pop()



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "weighting_factor"

    class function_block_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "function_block_name"
    # FCL.g:415:1: function_block_name : Identifier ;
    def function_block_name(self, ):

        retval = self.function_block_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:415:21: ( Identifier )
                # FCL.g:415:23: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_function_block_name1395)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "function_block_name"

    class rule_block_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "rule_block_name"
    # FCL.g:417:1: rule_block_name : Identifier ;
    def rule_block_name(self, ):

        retval = self.rule_block_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:417:17: ( Identifier )
                # FCL.g:417:19: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_rule_block_name1403)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "rule_block_name"

    class term_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "term_name"
    # FCL.g:418:1: term_name : Identifier ;
    def term_name(self, ):

        retval = self.term_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:418:11: ( Identifier )
                # FCL.g:418:13: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_term_name1411)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "term_name"

    class f_variable_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "f_variable_name"
    # FCL.g:419:1: f_variable_name : Identifier ;
    def f_variable_name(self, ):

        retval = self.f_variable_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:419:17: ( Identifier )
                # FCL.g:419:19: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_f_variable_name1419)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "f_variable_name"

    class variable_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "variable_name"
    # FCL.g:420:1: variable_name : Identifier ;
    def variable_name(self, ):

        retval = self.variable_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:420:15: ( Identifier )
                # FCL.g:420:17: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_variable_name1427)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "variable_name"

    class numeric_literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "numeric_literal"
    # FCL.g:421:1: numeric_literal : ( Integer_literal | Real_literal );
    def numeric_literal(self, ):

        retval = self.numeric_literal_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:421:17: ( Integer_literal | Real_literal )
                # FCL.g:
                pass 
                if (Integer_literal <= self.input.LA(1) <= Real_literal):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "numeric_literal"


    # Delegated rules


 

    FOLLOW_function_block_declaration_in_main45 = frozenset([1])
    FOLLOW_14_in_function_block_declaration60 = frozenset([4])
    FOLLOW_function_block_name_in_function_block_declaration65 = frozenset([15, 16, 21, 23, 24, 26, 28, 30])
    FOLLOW_type_definition_in_function_block_declaration71 = frozenset([15, 16, 21, 23, 24, 26, 28, 30])
    FOLLOW_fb_io_var_declarations_in_function_block_declaration76 = frozenset([15, 21, 23, 24, 26, 28, 30])
    FOLLOW_function_block_body_in_function_block_declaration82 = frozenset([15])
    FOLLOW_15_in_function_block_declaration86 = frozenset([])
    FOLLOW_EOF_in_function_block_declaration91 = frozenset([1])
    FOLLOW_16_in_type_definition103 = frozenset([4])
    FOLLOW_Identifier_in_type_definition105 = frozenset([4])
    FOLLOW_struct_element_in_type_definition109 = frozenset([4, 17])
    FOLLOW_17_in_type_definition113 = frozenset([1])
    FOLLOW_Identifier_in_struct_element125 = frozenset([18])
    FOLLOW_18_in_struct_element127 = frozenset([19])
    FOLLOW_19_in_struct_element129 = frozenset([20])
    FOLLOW_20_in_struct_element131 = frozenset([1])
    FOLLOW_input_declarations_in_fb_io_var_declarations145 = frozenset([1])
    FOLLOW_output_declarations_in_fb_io_var_declarations151 = frozenset([1])
    FOLLOW_21_in_input_declarations161 = frozenset([4])
    FOLLOW_var_decl_in_input_declarations163 = frozenset([4, 22])
    FOLLOW_22_in_input_declarations167 = frozenset([1])
    FOLLOW_23_in_output_declarations175 = frozenset([4])
    FOLLOW_var_decl_in_output_declarations177 = frozenset([4, 22])
    FOLLOW_22_in_output_declarations181 = frozenset([1])
    FOLLOW_Identifier_in_var_decl196 = frozenset([18])
    FOLLOW_18_in_var_decl201 = frozenset([4, 19])
    FOLLOW_type_in_var_decl206 = frozenset([20])
    FOLLOW_20_in_var_decl211 = frozenset([1])
    FOLLOW_19_in_type232 = frozenset([1])
    FOLLOW_Identifier_in_type240 = frozenset([1])
    FOLLOW_fuzzify_block_in_function_block_body263 = frozenset([1, 24, 26, 28, 30])
    FOLLOW_defuzzify_block_in_function_block_body269 = frozenset([1, 26, 28, 30])
    FOLLOW_rule_block_in_function_block_body278 = frozenset([1, 28, 30])
    FOLLOW_option_block_in_function_block_body284 = frozenset([1, 30])
    FOLLOW_24_in_fuzzify_block301 = frozenset([4])
    FOLLOW_variable_name_in_fuzzify_block307 = frozenset([25, 32])
    FOLLOW_linguistic_term_in_fuzzify_block312 = frozenset([25, 32])
    FOLLOW_25_in_fuzzify_block319 = frozenset([1])
    FOLLOW_26_in_defuzzify_block335 = frozenset([4])
    FOLLOW_f_variable_name_in_defuzzify_block341 = frozenset([32, 51])
    FOLLOW_linguistic_term_in_defuzzify_block346 = frozenset([32, 51])
    FOLLOW_accumulation_method_in_defuzzify_block353 = frozenset([37])
    FOLLOW_defuzzification_method_in_defuzzify_block358 = frozenset([27, 38, 40])
    FOLLOW_default_value_in_defuzzify_block364 = frozenset([27, 40])
    FOLLOW_range_in_defuzzify_block371 = frozenset([27])
    FOLLOW_27_in_defuzzify_block377 = frozenset([1])
    FOLLOW_28_in_rule_block394 = frozenset([4])
    FOLLOW_rule_block_name_in_rule_block401 = frozenset([6, 7, 29, 50, 56])
    FOLLOW_operator_definition_in_rule_block407 = frozenset([6, 7, 29, 50, 56])
    FOLLOW_activation_method_in_rule_block414 = frozenset([29, 56])
    FOLLOW_rule_in_rule_block421 = frozenset([29, 56])
    FOLLOW_29_in_rule_block428 = frozenset([1])
    FOLLOW_30_in_option_block437 = frozenset([31])
    FOLLOW_31_in_option_block441 = frozenset([1])
    FOLLOW_32_in_linguistic_term455 = frozenset([4])
    FOLLOW_term_name_in_linguistic_term457 = frozenset([33])
    FOLLOW_33_in_linguistic_term459 = frozenset([4, 8, 9, 34])
    FOLLOW_membership_function_in_linguistic_term461 = frozenset([20])
    FOLLOW_20_in_linguistic_term463 = frozenset([1])
    FOLLOW_singleton_in_membership_function484 = frozenset([1])
    FOLLOW_points_in_membership_function495 = frozenset([1])
    FOLLOW_numeric_literal_in_singleton516 = frozenset([1])
    FOLLOW_variable_name_in_singleton527 = frozenset([1])
    FOLLOW_34_in_points554 = frozenset([4, 8, 9])
    FOLLOW_numeric_literal_in_points563 = frozenset([35])
    FOLLOW_variable_name_in_points567 = frozenset([35])
    FOLLOW_35_in_points574 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_points582 = frozenset([36])
    FOLLOW_36_in_points588 = frozenset([1, 34])
    FOLLOW_37_in_defuzzification_method623 = frozenset([18])
    FOLLOW_18_in_defuzzification_method625 = frozenset([4])
    FOLLOW_Identifier_in_defuzzification_method629 = frozenset([20])
    FOLLOW_20_in_defuzzification_method634 = frozenset([1])
    FOLLOW_38_in_default_value649 = frozenset([33])
    FOLLOW_33_in_default_value651 = frozenset([8, 9, 39])
    FOLLOW_numeric_literal_in_default_value659 = frozenset([20])
    FOLLOW_39_in_default_value669 = frozenset([20])
    FOLLOW_20_in_default_value678 = frozenset([1])
    FOLLOW_40_in_range688 = frozenset([33])
    FOLLOW_33_in_range690 = frozenset([34])
    FOLLOW_34_in_range692 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_range694 = frozenset([41])
    FOLLOW_41_in_range696 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_range698 = frozenset([36])
    FOLLOW_36_in_range700 = frozenset([20])
    FOLLOW_20_in_range702 = frozenset([1])
    FOLLOW_Identifier_in_operator_name_any721 = frozenset([1, 42])
    FOLLOW_42_in_operator_name_any724 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_operator_name_any728 = frozenset([43])
    FOLLOW_43_in_operator_name_any730 = frozenset([1])
    FOLLOW_44_in_operator_name_AND751 = frozenset([1])
    FOLLOW_45_in_operator_name_AND761 = frozenset([1])
    FOLLOW_46_in_operator_name_AND772 = frozenset([1])
    FOLLOW_operator_name_any_in_operator_name_AND784 = frozenset([1])
    FOLLOW_47_in_operator_name_OR803 = frozenset([1])
    FOLLOW_48_in_operator_name_OR813 = frozenset([1])
    FOLLOW_49_in_operator_name_OR824 = frozenset([1])
    FOLLOW_operator_name_any_in_operator_name_OR836 = frozenset([1])
    FOLLOW_OR__in_operator_definition878 = frozenset([18])
    FOLLOW_18_in_operator_definition880 = frozenset([4, 47, 48, 49])
    FOLLOW_operator_name_OR_in_operator_definition884 = frozenset([20])
    FOLLOW_AND__in_operator_definition895 = frozenset([18])
    FOLLOW_18_in_operator_definition897 = frozenset([4, 44, 45, 46, 47, 48, 49])
    FOLLOW_operator_name_AND_in_operator_definition901 = frozenset([20])
    FOLLOW_20_in_operator_definition910 = frozenset([1])
    FOLLOW_50_in_activation_method919 = frozenset([18])
    FOLLOW_18_in_activation_method921 = frozenset([44, 45])
    FOLLOW_set_in_activation_method923 = frozenset([20])
    FOLLOW_20_in_activation_method931 = frozenset([1])
    FOLLOW_51_in_accumulation_method939 = frozenset([18])
    FOLLOW_18_in_accumulation_method941 = frozenset([47, 49, 52])
    FOLLOW_set_in_accumulation_method943 = frozenset([20])
    FOLLOW_20_in_accumulation_method955 = frozenset([1])
    FOLLOW_subcondition_in_condition983 = frozenset([1, 6, 7])
    FOLLOW_set_in_condition1005 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_subcondition_in_condition1022 = frozenset([1, 6, 7])
    FOLLOW_53_in_subcondition1055 = frozenset([34])
    FOLLOW_34_in_subcondition1057 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_subcondition1059 = frozenset([36])
    FOLLOW_36_in_subcondition1061 = frozenset([1])
    FOLLOW_subcondition2_in_subcondition1072 = frozenset([1])
    FOLLOW_34_in_subcondition21097 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_subcondition21101 = frozenset([36])
    FOLLOW_36_in_subcondition21103 = frozenset([1])
    FOLLOW_variable_name_in_subcondition21121 = frozenset([54, 55])
    FOLLOW_54_in_subcondition21124 = frozenset([4, 53])
    FOLLOW_53_in_subcondition21128 = frozenset([4])
    FOLLOW_55_in_subcondition21133 = frozenset([4])
    FOLLOW_term_name_in_subcondition21137 = frozenset([1])
    FOLLOW_operator_name_any_in_subcondition21155 = frozenset([34])
    FOLLOW_34_in_subcondition21157 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_subcondition21161 = frozenset([35])
    FOLLOW_35_in_subcondition21163 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_subcondition21167 = frozenset([36])
    FOLLOW_36_in_subcondition21169 = frozenset([1])
    FOLLOW_conclusion2_in_conclusion1211 = frozenset([1, 35])
    FOLLOW_35_in_conclusion1223 = frozenset([4, 34])
    FOLLOW_conclusion2_in_conclusion1227 = frozenset([1, 35])
    FOLLOW_34_in_conclusion21258 = frozenset([4, 34])
    FOLLOW_conclusion3_in_conclusion21262 = frozenset([36])
    FOLLOW_36_in_conclusion21265 = frozenset([1])
    FOLLOW_conclusion3_in_conclusion21284 = frozenset([1])
    FOLLOW_variable_name_in_conclusion31318 = frozenset([54])
    FOLLOW_54_in_conclusion31320 = frozenset([4])
    FOLLOW_term_name_in_conclusion31324 = frozenset([1])
    FOLLOW_56_in_rule1347 = frozenset([8])
    FOLLOW_Integer_literal_in_rule1349 = frozenset([18])
    FOLLOW_18_in_rule1351 = frozenset([57])
    FOLLOW_57_in_rule1353 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_rule1355 = frozenset([58])
    FOLLOW_58_in_rule1357 = frozenset([4, 34])
    FOLLOW_conclusion_in_rule1359 = frozenset([20, 59])
    FOLLOW_59_in_rule1362 = frozenset([8, 9])
    FOLLOW_weighting_factor_in_rule1364 = frozenset([20])
    FOLLOW_20_in_rule1370 = frozenset([1])
    FOLLOW_numeric_literal_in_weighting_factor1385 = frozenset([1])
    FOLLOW_Identifier_in_function_block_name1395 = frozenset([1])
    FOLLOW_Identifier_in_rule_block_name1403 = frozenset([1])
    FOLLOW_Identifier_in_term_name1411 = frozenset([1])
    FOLLOW_Identifier_in_f_variable_name1419 = frozenset([1])
    FOLLOW_Identifier_in_variable_name1427 = frozenset([1])
    FOLLOW_set_in_numeric_literal0 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FCLLexer", FCLParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
