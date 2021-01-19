
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "INT  program  :  change    program  :  program change    change  :  '.'\n                     |  '.' '~'\n                     |  '~' change    change  :  '^'\n                     |  '^' '{' INT '}'    change  :  '_'\n                     |  '_' '{' INT '}'    change  :  ':'    change  :  '>'    change  :  '<'   change  :  '*'  "
    
_lr_action_items = {'.':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,],[3,3,-1,-3,3,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),'~':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,],[4,4,-1,12,4,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),'^':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,],[5,5,-1,-3,5,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),'_':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,],[6,6,-1,-3,6,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),':':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,],[7,7,-1,-3,7,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),'>':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,],[8,8,-1,-3,8,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),'<':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,],[9,9,-1,-3,9,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),'*':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,19,],[10,10,-1,-3,10,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),'$end':([1,2,3,5,6,7,8,9,10,11,12,13,18,19,],[0,-1,-3,-6,-8,-10,-11,-12,-13,-2,-4,-5,-7,-9,]),'{':([5,6,],[14,15,]),'INT':([14,15,],[16,17,]),'}':([16,17,],[18,19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'change':([0,1,4,],[2,11,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> change','program',1,'p_program0','Parser.py',39),
  ('program -> program change','program',2,'p_program2','Parser.py',43),
  ('change -> .','change',1,'p_change0','Parser.py',49),
  ('change -> . ~','change',2,'p_change0','Parser.py',50),
  ('change -> ~ change','change',2,'p_change0','Parser.py',51),
  ('change -> ^','change',1,'p_change1','Parser.py',60),
  ('change -> ^ { INT }','change',4,'p_change1','Parser.py',61),
  ('change -> _','change',1,'p_change2','Parser.py',68),
  ('change -> _ { INT }','change',4,'p_change2','Parser.py',69),
  ('change -> :','change',1,'p_change3','Parser.py',76),
  ('change -> >','change',1,'p_change4','Parser.py',80),
  ('change -> <','change',1,'p_change5','Parser.py',84),
  ('change -> *','change',1,'p_change_7','Parser.py',88),
]