
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftADDSUBTRACTleftMULDIVkDIVkMODADD ASSIGN CHAR COLON COMMA DIV DOT DOUBLEDOT EQUAL GE GT ID INTEGER LB LE LP LT MUL RB REAL RP SEMICON STRING SUBTRACT SYS_CON SYS_FUNCT SYS_PROC SYS_TYPE UNEQUAL kAND kARRAY kBEGIN kCASE kCONST kDIV kDO kDOWNTO kELSE kEND kFOR kFUNCTION kGOTO kIF kIN kLABEL kMOD kNOT kOF kOR kPACKED kPROCEDURE kPROGRAM kREAD kRECORD kREPEAT kSET kTHEN kTO kTYPE kUNTIL kVAR kWHILE kWITHprogram :  program_head  routine  DOTprogram_head : kPROGRAM ID SEMICONroutine : routine_head routine_bodyroutine_head : const_part type_part var_part routine_partconst_part : kCONST const_expr_list\n                  | emptyconst_expr_list :  const_expr_list  const_expr\n                    |  const_exprconst_expr : ID EQUAL const_value SEMICONconst_value : INTEGERconst_value : REALconst_value : CHARconst_value : STRINGconst_value : SYS_CONtype_part : kTYPE type_decl_list\n                             | emptytype_decl_list :  type_decl_list  type_definition  \n                    |  type_definitiontype_definition :  ID  EQUAL  type_decl  SEMICONtype_decl :  simple_type_decl  \n                    |  array_type_decl  \n                    |  record_type_declsimple_type_decl : SYS_TYPEsimple_type_decl : LP name_list RPsimple_type_decl : const_value DOUBLEDOT const_valuesimple_type_decl : IDarray_type_decl :  kARRAY  LB  simple_type_decl  RB  kOF  type_declrecord_type_decl :  kRECORD  field_decl_list  kENDfield_decl_list :  field_decl_list  field_decl  \n                    |  field_declfield_decl :  name_list  COLON  type_decl  SEMICONname_list :  name_list  COMMA  ID  \n                    |  IDvar_part :  kVAR  var_decl_list  \n                    |  emptyvar_decl_list :  var_decl_list  var_decl  \n                    |  var_declvar_decl :  name_list  COLON  type_decl  SEMICONroutine_part :  routine_part  function_decl  \n                    |  routine_part  procedure_decl\n                    |  function_decl  \n                    |  procedure_decl  \n                    | emptysub_routine : routinefunction_decl : function_head  SEMICON  sub_routine  SEMICONfunction_head :  kFUNCTION  ID  parameters  COLON  simple_type_decl procedure_decl :  procedure_head  SEMICON  sub_routine  SEMICONprocedure_head :  kPROCEDURE ID parameters parameters :  LP  para_decl_list  RP  \n                    |  emptypara_decl_list :  para_decl_list  SEMICON  para_type_list \n                    | para_type_listpara_type_list :  var_para_list COLON  simple_type_declpara_type_list :  val_para_list COLON  simple_type_declvar_para_list :  kVAR  name_listval_para_list :  name_listroutine_body :  compound_stmtcompound_stmt :  kBEGIN  stmt_list  kENDstmt_list :  stmt_list  stmt  SEMICON  \n                    |  empty\n    stmt :  INTEGER  COLON  non_label_stmt\n         |  non_label_stmt\n    non_label_stmt :  assign_stmt \n                    | proc_stmt \n                    | compound_stmt \n                    | if_stmt \n                    | repeat_stmt \n                    | while_stmt \n                    | for_stmt \n                    | case_stmt \n                    | goto_stmt\n    assign_stmt : ID LB expression RB ASSIGN expression\n    \n    assign_stmt : ID  DOT  ID  ASSIGN  expression\n    assign_stmt :  ID  ASSIGN  expression proc_stmt :  ID\n                    |  ID  LP  args_list  RP\n                    |  SYS_PROC\n                    |  SYS_PROC  LP  expression_list  RP\n                    |  kREAD  LP  factor  RPif_stmt :  kIF  expression  kTHEN  stmt  else_clauseelse_clause :  kELSE stmt \n                    |  emptyrepeat_stmt :  kREPEAT  stmt_list  kUNTIL  expressionwhile_stmt :  kWHILE  expression  kDO stmtfor_stmt :  kFOR  ID  ASSIGN  expression  direction  expression  kDO stmtdirection :  kTO \n                    | kDOWNTOcase_stmt : kCASE expression kOF case_expr_list kENDcase_expr_list :  case_expr_list  case_expr  \n                    |  case_exprcase_expr :  const_value  COLON  stmt  SEMICON\n                    |  ID  COLON  stmt  SEMICONgoto_stmt :  kGOTO  INTEGERexpression_list :  expression_list  COMMA  expression\n                    |  expressionexpression :  expression  GE  expr  \n                    |  expression  GT  expr  \n                    |  expression  LE  expr\n                    |  expression  LT  expr  \n                    |  expression  EQUAL  expr  \n                    |  expression  UNEQUAL  expr  \n                    |  exprexpr :  expr  ADD  term  \n                    |  expr  SUBTRACT  term  \n                    |  expr  kOR  term  \n                    |  termterm :  term  MUL  factor\n                    |  term  kDIV factor\n                    |  term  DIV  factor  \n                    |  term  kMOD  factor\n                    |  term  kAND  factor  \n                    |  factor\n    factor  : ID  LP  args_list  RP\n            | SYS_FUNCT  LP  args_list  RP\n    \n    factor  : ID  LB  expression  RB\n    factor :  ID\n                    |  SYS_FUNCT\n                    |  const_value\n                    |  kNOT  factor\n                    |  SUBTRACT  factor  \n    factor : LP  expression  RPfactor : ID  DOT  IDargs_list :  args_list  COMMA  expression  \n            |  expressionempty :'
    
_lr_action_items = {'kPROGRAM':([0,],[3,]),'$end':([1,10,],[0,-1,]),'kCONST':([2,20,98,99,],[7,-2,7,7,]),'kTYPE':([2,6,8,17,18,20,29,98,99,115,],[-125,15,-6,-5,-8,-2,-7,-125,-125,-9,]),'kVAR':([2,6,8,14,16,17,18,20,26,27,29,65,98,99,115,155,160,236,],[-125,-125,-6,24,-16,-5,-8,-2,-15,-18,-7,-17,-125,-125,-9,208,-19,208,]),'kFUNCTION':([2,6,8,14,16,17,18,20,23,25,26,27,29,53,54,55,56,61,62,65,96,97,98,99,102,115,160,201,202,210,],[-125,-125,-6,-125,-16,-5,-8,-2,59,-35,-15,-18,-7,59,-41,-42,-43,-34,-37,-17,-39,-40,-125,-125,-36,-9,-19,-45,-47,-38,]),'kPROCEDURE':([2,6,8,14,16,17,18,20,23,25,26,27,29,53,54,55,56,61,62,65,96,97,98,99,102,115,160,201,202,210,],[-125,-125,-6,-125,-16,-5,-8,-2,60,-35,-15,-18,-7,60,-41,-42,-43,-34,-37,-17,-39,-40,-125,-125,-36,-9,-19,-45,-47,-38,]),'kBEGIN':([2,5,6,8,13,14,16,17,18,20,21,22,23,25,26,27,29,48,53,54,55,56,61,62,65,73,74,91,96,97,98,99,102,115,125,148,160,201,202,210,222,232,233,252,],[-125,13,-125,-6,-125,-125,-16,-5,-8,-2,13,-60,-125,-35,-15,-18,-7,-125,-4,-41,-42,-43,-34,-37,-17,-59,13,13,-39,-40,-125,-125,-36,-9,13,13,-19,-45,-47,-38,13,13,13,13,]),'ID':([3,7,13,15,17,18,21,22,24,26,27,29,47,48,49,50,51,59,60,61,62,65,66,73,74,75,76,77,78,79,80,84,87,90,91,102,103,104,111,114,115,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,143,145,147,148,149,150,155,160,163,164,165,168,170,172,197,198,203,208,210,215,216,217,222,227,228,229,231,232,233,236,237,238,250,251,252,253,254,],[9,19,-125,28,19,-8,44,-60,64,28,-18,-7,86,-125,86,93,86,100,101,64,-37,-17,105,-59,44,86,86,119,86,86,86,86,86,86,44,-36,105,159,64,64,-9,44,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,191,86,86,44,86,200,64,-19,105,64,-30,86,86,86,200,-90,105,64,-38,-29,105,86,44,86,-86,-87,-89,44,44,64,105,105,105,-31,44,-91,-92,]),'DOT':([4,11,12,31,44,86,],[10,-3,-57,-58,77,143,]),'SEMICON':([9,11,12,31,32,34,35,36,37,38,39,40,41,42,43,44,45,57,58,67,68,69,70,71,72,82,83,85,86,88,89,95,101,105,106,107,108,109,110,116,118,140,146,151,152,153,156,157,158,169,171,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,194,195,204,205,211,212,214,218,221,223,224,225,226,230,234,235,241,242,243,245,246,247,248,249,255,256,],[20,-3,-57,-58,73,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-75,-77,98,99,115,-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,-93,-125,-26,160,-20,-21,-22,-23,-61,-74,-120,-119,201,-44,202,-50,-48,210,-76,-78,-79,-125,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,-83,-84,236,-52,-24,-25,-28,-73,-80,-82,-113,-115,-114,-88,-46,-49,251,-72,-81,253,254,-51,-53,-54,-27,-85,]),'kEND':([13,21,22,73,164,165,197,198,215,231,251,253,254,],[-125,31,-60,-59,214,-30,230,-90,-29,-89,-31,-91,-92,]),'INTEGER':([13,21,22,30,47,48,49,51,52,66,73,75,76,78,79,80,84,87,90,91,103,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,148,149,150,162,163,168,170,172,197,198,203,216,217,222,227,228,229,231,232,233,237,238,250,252,253,254,],[-125,33,-60,68,68,-125,68,68,95,68,-59,68,68,68,68,68,68,68,68,33,68,33,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,33,68,68,68,68,68,68,68,68,-90,68,68,68,33,68,-86,-87,-89,33,33,68,68,68,33,-91,-92,]),'SYS_PROC':([13,21,22,48,73,74,91,125,148,222,232,233,252,],[-125,45,-60,-125,-59,45,45,45,45,45,45,45,45,]),'kREAD':([13,21,22,48,73,74,91,125,148,222,232,233,252,],[-125,46,-60,-125,-59,46,46,46,46,46,46,46,46,]),'kIF':([13,21,22,48,73,74,91,125,148,222,232,233,252,],[-125,47,-60,-125,-59,47,47,47,47,47,47,47,47,]),'kREPEAT':([13,21,22,48,73,74,91,125,148,222,232,233,252,],[-125,48,-60,-125,-59,48,48,48,48,48,48,48,48,]),'kWHILE':([13,21,22,48,73,74,91,125,148,222,232,233,252,],[-125,49,-60,-125,-59,49,49,49,49,49,49,49,49,]),'kFOR':([13,21,22,48,73,74,91,125,148,222,232,233,252,],[-125,50,-60,-125,-59,50,50,50,50,50,50,50,50,]),'kCASE':([13,21,22,48,73,74,91,125,148,222,232,233,252,],[-125,51,-60,-125,-59,51,51,51,51,51,51,51,51,]),'kGOTO':([13,21,22,48,73,74,91,125,148,222,232,233,252,],[-125,52,-60,-125,-59,52,52,52,52,52,52,52,52,]),'EQUAL':([19,28,68,69,70,71,72,81,82,83,85,86,88,89,92,94,117,118,121,123,140,144,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,190,191,192,194,196,218,219,220,224,225,226,242,244,],[30,66,-10,-11,-12,-13,-14,130,-102,-106,-112,-116,-117,-118,130,130,130,130,130,130,-120,130,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,130,-122,-121,130,130,130,130,130,-113,-115,-114,130,130,]),'kUNTIL':([22,48,73,91,],[-60,-125,-59,147,]),'REAL':([30,47,49,51,66,75,76,78,79,80,84,87,90,103,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,150,162,163,168,170,172,197,198,203,216,217,227,228,229,231,237,238,250,253,254,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,-90,69,69,69,69,-86,-87,-89,69,69,69,-91,-92,]),'CHAR':([30,47,49,51,66,75,76,78,79,80,84,87,90,103,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,150,162,163,168,170,172,197,198,203,216,217,227,228,229,231,237,238,250,253,254,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-90,70,70,70,70,-86,-87,-89,70,70,70,-91,-92,]),'STRING':([30,47,49,51,66,75,76,78,79,80,84,87,90,103,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,150,162,163,168,170,172,197,198,203,216,217,227,228,229,231,237,238,250,253,254,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-90,71,71,71,71,-86,-87,-89,71,71,71,-91,-92,]),'SYS_CON':([30,47,49,51,66,75,76,78,79,80,84,87,90,103,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,150,162,163,168,170,172,197,198,203,216,217,227,228,229,231,237,238,250,253,254,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-90,72,72,72,72,-86,-87,-89,72,72,72,-91,-92,]),'kELSE':([31,34,35,36,37,38,39,40,41,42,43,44,45,68,69,70,71,72,82,83,85,86,88,89,95,116,118,140,146,169,171,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,194,195,218,221,223,224,225,226,230,242,243,256,],[-58,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-75,-77,-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,-93,-61,-74,-120,-119,-76,-78,-79,222,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,-83,-84,-73,-80,-82,-113,-115,-114,-88,-72,-81,-85,]),'COLON':([33,63,64,68,69,70,71,72,100,154,156,159,166,199,200,206,207,209,235,239,],[74,103,-33,-10,-11,-12,-13,-14,-125,203,-50,-32,216,232,233,237,238,-56,-49,-55,]),'LB':([44,86,113,],[75,142,163,]),'ASSIGN':([44,93,119,167,],[76,149,168,217,]),'LP':([44,45,46,47,49,51,66,75,76,78,79,80,84,86,87,88,90,100,101,103,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,163,168,170,172,203,216,217,227,228,229,237,238,250,],[78,79,80,87,87,87,111,87,87,87,87,87,87,141,87,145,87,155,155,111,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,111,87,87,87,111,111,87,87,-86,-87,111,111,111,]),'SYS_FUNCT':([47,49,51,75,76,78,79,80,84,87,90,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,168,170,172,217,227,228,229,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,-86,-87,]),'kNOT':([47,49,51,75,76,78,79,80,84,87,90,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,168,170,172,217,227,228,229,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,-86,-87,]),'SUBTRACT':([47,49,51,68,69,70,71,72,75,76,78,79,80,82,83,84,85,86,87,88,89,90,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,146,147,149,168,170,172,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,217,224,225,226,227,228,229,],[84,84,84,-10,-11,-12,-13,-14,84,84,84,84,84,133,-106,84,-112,-116,84,-117,-118,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,-120,84,84,84,-119,84,84,84,84,84,133,133,133,133,133,133,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,84,-113,-115,-114,84,-86,-87,]),'COMMA':([63,64,68,69,70,71,72,82,83,85,86,88,89,120,121,122,123,140,146,159,161,166,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,191,192,193,209,219,220,224,225,226,239,],[104,-33,-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,170,-124,172,-95,-120,-119,-32,104,104,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,170,-122,-121,170,104,-123,-94,-113,-115,-114,104,]),'RP':([64,68,69,70,71,72,82,83,85,86,88,89,105,110,120,121,122,123,124,140,144,146,159,161,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,191,192,193,204,205,211,212,219,220,224,225,226,247,248,249,],[-33,-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,-26,-23,169,-124,171,-95,173,-120,192,-119,-32,211,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,224,-122,-121,226,235,-52,-24,-25,-123,-94,-113,-115,-114,-51,-53,-54,]),'SYS_TYPE':([66,103,163,203,216,237,238,250,],[110,110,110,110,110,110,110,110,]),'kARRAY':([66,103,216,250,],[113,113,113,113,]),'kRECORD':([66,103,216,250,],[114,114,114,114,]),'MUL':([68,69,70,71,72,83,85,86,88,89,140,146,181,182,183,184,185,186,187,188,191,192,224,225,226,],[-10,-11,-12,-13,-14,135,-112,-116,-117,-118,-120,-119,135,135,135,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,]),'kDIV':([68,69,70,71,72,83,85,86,88,89,140,146,181,182,183,184,185,186,187,188,191,192,224,225,226,],[-10,-11,-12,-13,-14,136,-112,-116,-117,-118,-120,-119,136,136,136,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,]),'DIV':([68,69,70,71,72,83,85,86,88,89,140,146,181,182,183,184,185,186,187,188,191,192,224,225,226,],[-10,-11,-12,-13,-14,137,-112,-116,-117,-118,-120,-119,137,137,137,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,]),'kMOD':([68,69,70,71,72,83,85,86,88,89,140,146,181,182,183,184,185,186,187,188,191,192,224,225,226,],[-10,-11,-12,-13,-14,138,-112,-116,-117,-118,-120,-119,138,138,138,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,]),'kAND':([68,69,70,71,72,83,85,86,88,89,140,146,181,182,183,184,185,186,187,188,191,192,224,225,226,],[-10,-11,-12,-13,-14,139,-112,-116,-117,-118,-120,-119,139,139,139,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,]),'ADD':([68,69,70,71,72,82,83,85,86,88,89,140,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,224,225,226,],[-10,-11,-12,-13,-14,132,-106,-112,-116,-117,-118,-120,-119,132,132,132,132,132,132,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,]),'kOR':([68,69,70,71,72,82,83,85,86,88,89,140,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,224,225,226,],[-10,-11,-12,-13,-14,134,-106,-112,-116,-117,-118,-120,-119,134,134,134,134,134,134,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,]),'kTHEN':([68,69,70,71,72,81,82,83,85,86,88,89,140,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,224,225,226,],[-10,-11,-12,-13,-14,125,-102,-106,-112,-116,-117,-118,-120,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,]),'GE':([68,69,70,71,72,81,82,83,85,86,88,89,92,94,117,118,121,123,140,144,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,190,191,192,194,196,218,219,220,224,225,226,242,244,],[-10,-11,-12,-13,-14,126,-102,-106,-112,-116,-117,-118,126,126,126,126,126,126,-120,126,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,126,-122,-121,126,126,126,126,126,-113,-115,-114,126,126,]),'GT':([68,69,70,71,72,81,82,83,85,86,88,89,92,94,117,118,121,123,140,144,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,190,191,192,194,196,218,219,220,224,225,226,242,244,],[-10,-11,-12,-13,-14,127,-102,-106,-112,-116,-117,-118,127,127,127,127,127,127,-120,127,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,127,-122,-121,127,127,127,127,127,-113,-115,-114,127,127,]),'LE':([68,69,70,71,72,81,82,83,85,86,88,89,92,94,117,118,121,123,140,144,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,190,191,192,194,196,218,219,220,224,225,226,242,244,],[-10,-11,-12,-13,-14,128,-102,-106,-112,-116,-117,-118,128,128,128,128,128,128,-120,128,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,128,-122,-121,128,128,128,128,128,-113,-115,-114,128,128,]),'LT':([68,69,70,71,72,81,82,83,85,86,88,89,92,94,117,118,121,123,140,144,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,190,191,192,194,196,218,219,220,224,225,226,242,244,],[-10,-11,-12,-13,-14,129,-102,-106,-112,-116,-117,-118,129,129,129,129,129,129,-120,129,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,129,-122,-121,129,129,129,129,129,-113,-115,-114,129,129,]),'UNEQUAL':([68,69,70,71,72,81,82,83,85,86,88,89,92,94,117,118,121,123,140,144,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,190,191,192,194,196,218,219,220,224,225,226,242,244,],[-10,-11,-12,-13,-14,131,-102,-106,-112,-116,-117,-118,131,131,131,131,131,131,-120,131,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,131,-122,-121,131,131,131,131,131,-113,-115,-114,131,131,]),'kDO':([68,69,70,71,72,82,83,85,86,88,89,92,140,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,224,225,226,244,],[-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,148,-120,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,252,]),'kOF':([68,69,70,71,72,82,83,85,86,88,89,94,140,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,224,225,226,240,],[-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,150,-120,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,-113,-115,-114,250,]),'DOUBLEDOT':([68,69,70,71,72,112,],[-10,-11,-12,-13,-14,162,]),'RB':([68,69,70,71,72,82,83,85,86,88,89,105,110,117,140,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,190,191,192,211,212,213,224,225,226,],[-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,-26,-23,167,-120,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,225,-122,-121,-24,-25,240,-113,-115,-114,]),'kTO':([68,69,70,71,72,82,83,85,86,88,89,140,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,196,224,225,226,],[-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,-120,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,228,-113,-115,-114,]),'kDOWNTO':([68,69,70,71,72,82,83,85,86,88,89,140,146,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,196,224,225,226,],[-10,-11,-12,-13,-14,-102,-106,-112,-116,-117,-118,-120,-119,-96,-97,-98,-99,-100,-101,-103,-104,-105,-107,-108,-109,-110,-111,-122,-121,229,-113,-115,-114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_head':([0,],[2,]),'routine':([2,98,99,],[4,152,152,]),'routine_head':([2,98,99,],[5,5,5,]),'const_part':([2,98,99,],[6,6,6,]),'empty':([2,6,13,14,23,48,98,99,100,101,174,],[8,16,22,25,56,22,8,8,156,156,223,]),'routine_body':([5,],[11,]),'compound_stmt':([5,21,74,91,125,148,222,232,233,252,],[12,37,37,37,37,37,37,37,37,37,]),'type_part':([6,],[14,]),'const_expr_list':([7,],[17,]),'const_expr':([7,17,],[18,29,]),'stmt_list':([13,48,],[21,91,]),'var_part':([14,],[23,]),'type_decl_list':([15,],[26,]),'type_definition':([15,26,],[27,65,]),'stmt':([21,91,125,148,222,232,233,252,],[32,32,174,195,243,245,246,256,]),'non_label_stmt':([21,74,91,125,148,222,232,233,252,],[34,116,34,34,34,34,34,34,34,]),'assign_stmt':([21,74,91,125,148,222,232,233,252,],[35,35,35,35,35,35,35,35,35,]),'proc_stmt':([21,74,91,125,148,222,232,233,252,],[36,36,36,36,36,36,36,36,36,]),'if_stmt':([21,74,91,125,148,222,232,233,252,],[38,38,38,38,38,38,38,38,38,]),'repeat_stmt':([21,74,91,125,148,222,232,233,252,],[39,39,39,39,39,39,39,39,39,]),'while_stmt':([21,74,91,125,148,222,232,233,252,],[40,40,40,40,40,40,40,40,40,]),'for_stmt':([21,74,91,125,148,222,232,233,252,],[41,41,41,41,41,41,41,41,41,]),'case_stmt':([21,74,91,125,148,222,232,233,252,],[42,42,42,42,42,42,42,42,42,]),'goto_stmt':([21,74,91,125,148,222,232,233,252,],[43,43,43,43,43,43,43,43,43,]),'routine_part':([23,],[53,]),'function_decl':([23,53,],[54,96,]),'procedure_decl':([23,53,],[55,97,]),'function_head':([23,53,],[57,57,]),'procedure_head':([23,53,],[58,58,]),'var_decl_list':([24,],[61,]),'var_decl':([24,61,],[62,102,]),'name_list':([24,61,111,114,155,164,208,236,],[63,63,161,166,209,166,239,209,]),'const_value':([30,47,49,51,66,75,76,78,79,80,84,87,90,103,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,150,162,163,168,170,172,197,203,216,217,227,237,238,250,],[67,89,89,89,112,89,89,89,89,89,89,89,89,112,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,199,212,112,89,89,89,199,112,112,89,89,112,112,112,]),'expression':([47,49,51,75,76,78,79,87,141,142,145,147,149,168,170,172,217,227,],[81,92,94,117,118,121,123,144,121,190,121,194,196,218,219,220,242,244,]),'expr':([47,49,51,75,76,78,79,87,126,127,128,129,130,131,141,142,145,147,149,168,170,172,217,227,],[82,82,82,82,82,82,82,82,175,176,177,178,179,180,82,82,82,82,82,82,82,82,82,82,]),'term':([47,49,51,75,76,78,79,87,126,127,128,129,130,131,132,133,134,141,142,145,147,149,168,170,172,217,227,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,181,182,183,83,83,83,83,83,83,83,83,83,83,]),'factor':([47,49,51,75,76,78,79,80,84,87,90,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,145,147,149,168,170,172,217,227,],[85,85,85,85,85,85,85,124,140,85,146,85,85,85,85,85,85,85,85,85,184,185,186,187,188,85,85,85,85,85,85,85,85,85,85,]),'type_decl':([66,103,216,250,],[106,158,241,255,]),'simple_type_decl':([66,103,163,203,216,237,238,250,],[107,107,213,234,107,248,249,107,]),'array_type_decl':([66,103,216,250,],[108,108,108,108,]),'record_type_decl':([66,103,216,250,],[109,109,109,109,]),'args_list':([78,141,145,],[120,189,193,]),'expression_list':([79,],[122,]),'sub_routine':([98,99,],[151,153,]),'parameters':([100,101,],[154,157,]),'field_decl_list':([114,],[164,]),'field_decl':([114,164,],[165,215,]),'case_expr_list':([150,],[197,]),'case_expr':([150,197,],[198,231,]),'para_decl_list':([155,],[204,]),'para_type_list':([155,236,],[205,247,]),'var_para_list':([155,236,],[206,206,]),'val_para_list':([155,236,],[207,207,]),'else_clause':([174,],[221,]),'direction':([196,],[227,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_head routine DOT','program',3,'p_program','yacc_pas.py',17),
  ('program_head -> kPROGRAM ID SEMICON','program_head',3,'p_program_head','yacc_pas.py',22),
  ('routine -> routine_head routine_body','routine',2,'p_routine','yacc_pas.py',27),
  ('routine_head -> const_part type_part var_part routine_part','routine_head',4,'p_routine_head','yacc_pas.py',32),
  ('const_part -> kCONST const_expr_list','const_part',2,'p_const_part','yacc_pas.py',37),
  ('const_part -> empty','const_part',1,'p_const_part','yacc_pas.py',38),
  ('const_expr_list -> const_expr_list const_expr','const_expr_list',2,'p_const_expr_list','yacc_pas.py',44),
  ('const_expr_list -> const_expr','const_expr_list',1,'p_const_expr_list','yacc_pas.py',45),
  ('const_expr -> ID EQUAL const_value SEMICON','const_expr',4,'p_const_expr','yacc_pas.py',53),
  ('const_value -> INTEGER','const_value',1,'p_const_value_1','yacc_pas.py',60),
  ('const_value -> REAL','const_value',1,'p_const_value_2','yacc_pas.py',65),
  ('const_value -> CHAR','const_value',1,'p_const_value_3','yacc_pas.py',70),
  ('const_value -> STRING','const_value',1,'p_const_value_4','yacc_pas.py',76),
  ('const_value -> SYS_CON','const_value',1,'p_const_value_5','yacc_pas.py',81),
  ('type_part -> kTYPE type_decl_list','type_part',2,'p_type_part','yacc_pas.py',87),
  ('type_part -> empty','type_part',1,'p_type_part','yacc_pas.py',88),
  ('type_decl_list -> type_decl_list type_definition','type_decl_list',2,'p_type_decl_list','yacc_pas.py',94),
  ('type_decl_list -> type_definition','type_decl_list',1,'p_type_decl_list','yacc_pas.py',95),
  ('type_definition -> ID EQUAL type_decl SEMICON','type_definition',4,'p_type_definition','yacc_pas.py',103),
  ('type_decl -> simple_type_decl','type_decl',1,'p_type_decl','yacc_pas.py',108),
  ('type_decl -> array_type_decl','type_decl',1,'p_type_decl','yacc_pas.py',109),
  ('type_decl -> record_type_decl','type_decl',1,'p_type_decl','yacc_pas.py',110),
  ('simple_type_decl -> SYS_TYPE','simple_type_decl',1,'p_simple_type_decl_1','yacc_pas.py',125),
  ('simple_type_decl -> LP name_list RP','simple_type_decl',3,'p_simple_type_decl_2','yacc_pas.py',131),
  ('simple_type_decl -> const_value DOUBLEDOT const_value','simple_type_decl',3,'p_simple_type_decl_3','yacc_pas.py',136),
  ('simple_type_decl -> ID','simple_type_decl',1,'p_simple_type_decl_4','yacc_pas.py',142),
  ('array_type_decl -> kARRAY LB simple_type_decl RB kOF type_decl','array_type_decl',6,'p_array_type_decl','yacc_pas.py',148),
  ('record_type_decl -> kRECORD field_decl_list kEND','record_type_decl',3,'p_record_type_decl','yacc_pas.py',153),
  ('field_decl_list -> field_decl_list field_decl','field_decl_list',2,'p_field_decl_list','yacc_pas.py',158),
  ('field_decl_list -> field_decl','field_decl_list',1,'p_field_decl_list','yacc_pas.py',159),
  ('field_decl -> name_list COLON type_decl SEMICON','field_decl',4,'p_field_decl','yacc_pas.py',167),
  ('name_list -> name_list COMMA ID','name_list',3,'p_name_list','yacc_pas.py',172),
  ('name_list -> ID','name_list',1,'p_name_list','yacc_pas.py',173),
  ('var_part -> kVAR var_decl_list','var_part',2,'p_var_part','yacc_pas.py',182),
  ('var_part -> empty','var_part',1,'p_var_part','yacc_pas.py',183),
  ('var_decl_list -> var_decl_list var_decl','var_decl_list',2,'p_var_decl_list','yacc_pas.py',189),
  ('var_decl_list -> var_decl','var_decl_list',1,'p_var_decl_list','yacc_pas.py',190),
  ('var_decl -> name_list COLON type_decl SEMICON','var_decl',4,'p_var_decl','yacc_pas.py',198),
  ('routine_part -> routine_part function_decl','routine_part',2,'p_routine_part','yacc_pas.py',204),
  ('routine_part -> routine_part procedure_decl','routine_part',2,'p_routine_part','yacc_pas.py',205),
  ('routine_part -> function_decl','routine_part',1,'p_routine_part','yacc_pas.py',206),
  ('routine_part -> procedure_decl','routine_part',1,'p_routine_part','yacc_pas.py',207),
  ('routine_part -> empty','routine_part',1,'p_routine_part','yacc_pas.py',208),
  ('sub_routine -> routine','sub_routine',1,'p_sub_routine','yacc_pas.py',217),
  ('function_decl -> function_head SEMICON sub_routine SEMICON','function_decl',4,'p_function_decl','yacc_pas.py',222),
  ('function_head -> kFUNCTION ID parameters COLON simple_type_decl','function_head',5,'p_function_head','yacc_pas.py',227),
  ('procedure_decl -> procedure_head SEMICON sub_routine SEMICON','procedure_decl',4,'p_procedure_decl','yacc_pas.py',232),
  ('procedure_head -> kPROCEDURE ID parameters','procedure_head',3,'p_procedure_head','yacc_pas.py',237),
  ('parameters -> LP para_decl_list RP','parameters',3,'p_parameters','yacc_pas.py',242),
  ('parameters -> empty','parameters',1,'p_parameters','yacc_pas.py',243),
  ('para_decl_list -> para_decl_list SEMICON para_type_list','para_decl_list',3,'p_para_decl_list','yacc_pas.py',249),
  ('para_decl_list -> para_type_list','para_decl_list',1,'p_para_decl_list','yacc_pas.py',250),
  ('para_type_list -> var_para_list COLON simple_type_decl','para_type_list',3,'p_var_para_type_list','yacc_pas.py',258),
  ('para_type_list -> val_para_list COLON simple_type_decl','para_type_list',3,'p_val_para_type_list','yacc_pas.py',263),
  ('var_para_list -> kVAR name_list','var_para_list',2,'p_var_para_list_0','yacc_pas.py',268),
  ('val_para_list -> name_list','val_para_list',1,'p_val_para_list_1','yacc_pas.py',273),
  ('routine_body -> compound_stmt','routine_body',1,'p_routine_body','yacc_pas.py',278),
  ('compound_stmt -> kBEGIN stmt_list kEND','compound_stmt',3,'p_compound_stmt','yacc_pas.py',283),
  ('stmt_list -> stmt_list stmt SEMICON','stmt_list',3,'p_stmt_list','yacc_pas.py',288),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','yacc_pas.py',289),
  ('stmt -> INTEGER COLON non_label_stmt','stmt',3,'p_stmt','yacc_pas.py',298),
  ('stmt -> non_label_stmt','stmt',1,'p_stmt','yacc_pas.py',299),
  ('non_label_stmt -> assign_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',309),
  ('non_label_stmt -> proc_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',310),
  ('non_label_stmt -> compound_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',311),
  ('non_label_stmt -> if_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',312),
  ('non_label_stmt -> repeat_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',313),
  ('non_label_stmt -> while_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',314),
  ('non_label_stmt -> for_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',315),
  ('non_label_stmt -> case_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',316),
  ('non_label_stmt -> goto_stmt','non_label_stmt',1,'p_non_label_stmt','yacc_pas.py',317),
  ('assign_stmt -> ID LB expression RB ASSIGN expression','assign_stmt',6,'p_assign_stmt_arr','yacc_pas.py',323),
  ('assign_stmt -> ID DOT ID ASSIGN expression','assign_stmt',5,'p_assign_stmt_record','yacc_pas.py',330),
  ('assign_stmt -> ID ASSIGN expression','assign_stmt',3,'p_assign_stmt','yacc_pas.py',336),
  ('proc_stmt -> ID','proc_stmt',1,'p_proc_stmt','yacc_pas.py',343),
  ('proc_stmt -> ID LP args_list RP','proc_stmt',4,'p_proc_stmt','yacc_pas.py',344),
  ('proc_stmt -> SYS_PROC','proc_stmt',1,'p_proc_stmt','yacc_pas.py',345),
  ('proc_stmt -> SYS_PROC LP expression_list RP','proc_stmt',4,'p_proc_stmt','yacc_pas.py',346),
  ('proc_stmt -> kREAD LP factor RP','proc_stmt',4,'p_proc_stmt','yacc_pas.py',347),
  ('if_stmt -> kIF expression kTHEN stmt else_clause','if_stmt',5,'p_if_stmt','yacc_pas.py',355),
  ('else_clause -> kELSE stmt','else_clause',2,'p_else_clause','yacc_pas.py',360),
  ('else_clause -> empty','else_clause',1,'p_else_clause','yacc_pas.py',361),
  ('repeat_stmt -> kREPEAT stmt_list kUNTIL expression','repeat_stmt',4,'p_repeat_stmt','yacc_pas.py',367),
  ('while_stmt -> kWHILE expression kDO stmt','while_stmt',4,'p_while_stmt','yacc_pas.py',372),
  ('for_stmt -> kFOR ID ASSIGN expression direction expression kDO stmt','for_stmt',8,'p_for_stmt','yacc_pas.py',377),
  ('direction -> kTO','direction',1,'p_direction','yacc_pas.py',382),
  ('direction -> kDOWNTO','direction',1,'p_direction','yacc_pas.py',383),
  ('case_stmt -> kCASE expression kOF case_expr_list kEND','case_stmt',5,'p_case_stmt','yacc_pas.py',388),
  ('case_expr_list -> case_expr_list case_expr','case_expr_list',2,'p_case_expr_list','yacc_pas.py',393),
  ('case_expr_list -> case_expr','case_expr_list',1,'p_case_expr_list','yacc_pas.py',394),
  ('case_expr -> const_value COLON stmt SEMICON','case_expr',4,'p_case_expr','yacc_pas.py',402),
  ('case_expr -> ID COLON stmt SEMICON','case_expr',4,'p_case_expr','yacc_pas.py',403),
  ('goto_stmt -> kGOTO INTEGER','goto_stmt',2,'p_goto_stmt','yacc_pas.py',408),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','yacc_pas.py',413),
  ('expression_list -> expression','expression_list',1,'p_expression_list','yacc_pas.py',414),
  ('expression -> expression GE expr','expression',3,'p_expression','yacc_pas.py',422),
  ('expression -> expression GT expr','expression',3,'p_expression','yacc_pas.py',423),
  ('expression -> expression LE expr','expression',3,'p_expression','yacc_pas.py',424),
  ('expression -> expression LT expr','expression',3,'p_expression','yacc_pas.py',425),
  ('expression -> expression EQUAL expr','expression',3,'p_expression','yacc_pas.py',426),
  ('expression -> expression UNEQUAL expr','expression',3,'p_expression','yacc_pas.py',427),
  ('expression -> expr','expression',1,'p_expression','yacc_pas.py',428),
  ('expr -> expr ADD term','expr',3,'p_expr','yacc_pas.py',440),
  ('expr -> expr SUBTRACT term','expr',3,'p_expr','yacc_pas.py',441),
  ('expr -> expr kOR term','expr',3,'p_expr','yacc_pas.py',442),
  ('expr -> term','expr',1,'p_expr','yacc_pas.py',443),
  ('term -> term MUL factor','term',3,'p_term','yacc_pas.py',455),
  ('term -> term kDIV factor','term',3,'p_term','yacc_pas.py',456),
  ('term -> term DIV factor','term',3,'p_term','yacc_pas.py',457),
  ('term -> term kMOD factor','term',3,'p_term','yacc_pas.py',458),
  ('term -> term kAND factor','term',3,'p_term','yacc_pas.py',459),
  ('term -> factor','term',1,'p_term','yacc_pas.py',460),
  ('factor -> ID LP args_list RP','factor',4,'p_factor_func','yacc_pas.py',477),
  ('factor -> SYS_FUNCT LP args_list RP','factor',4,'p_factor_func','yacc_pas.py',478),
  ('factor -> ID LB expression RB','factor',4,'p_factor_arr','yacc_pas.py',485),
  ('factor -> ID','factor',1,'p_factor_1','yacc_pas.py',491),
  ('factor -> SYS_FUNCT','factor',1,'p_factor_1','yacc_pas.py',492),
  ('factor -> const_value','factor',1,'p_factor_1','yacc_pas.py',493),
  ('factor -> kNOT factor','factor',2,'p_factor_1','yacc_pas.py',494),
  ('factor -> SUBTRACT factor','factor',2,'p_factor_1','yacc_pas.py',495),
  ('factor -> LP expression RP','factor',3,'p_factor_2','yacc_pas.py',506),
  ('factor -> ID DOT ID','factor',3,'p_factor3','yacc_pas.py',511),
  ('args_list -> args_list COMMA expression','args_list',3,'p_args_list','yacc_pas.py',516),
  ('args_list -> expression','args_list',1,'p_args_list','yacc_pas.py',517),
  ('empty -> <empty>','empty',0,'p_empty','yacc_pas.py',527),
]
