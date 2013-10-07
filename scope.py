#!/usr/bin/env python

scope = {
	
	'base' : {
		"PARENS" 					:	[('type', '()')],
		"BRACKETS" 					:	[('type', '[]')],
		"BRACES" 					:	[('type', '{}')],
		"BACKTICK" 					:	[('type', '`')],
		"QUOTE" 					:	[('type', '"')],
		"SINGLE-QUOTE"				:	[('type', '\'')]
		"DOT" 						:	[('type', '.')],
		"COMMA" 					:	[('type', ',')],
		"COLON" 					:	[('type', ':')],
		"SEMI-COLON" 				:	[('type', ';')],
		"ELIPSIS" 					:	[('type', '...')],
		"SPACE" 					:	[('type', ' ')],
		"TAB" 						:	[('key', 'Tab')],
		"RETURN" 					:	[('key', 'Return')],
		"PLUS" 						:	[('type', '+')],
		"MINUS" 					:	[('type', '-')],
		"GREATER-THAN" 				:	[('type', '>')],
		"LESS-THAN" 				:	[('type', '<')],
		"IS-EQUAL-TO" 				:	[('type', '==')],
		"GREATER-THAN-OR-EQUAL-TO" 	:	[('type', '==')],
		"LESS-THAN-OR-EQUAL-TO" 	:	[('type', '==')],
		"EQUALS" 					:	[('type', '=')],
		"TIMES" 					:	[('type', '*')],
		"DIVIDE" 					:	[('type', '/')],
		"REMAINDER" 				:	[('type', '%')]
		
	},

	'letters' : {
		"ALPHA" 					:	[('type', 'a')],
		"BRAVO" 					:	[('type', 'b')],
		"CHARLIE" 					:	[('type', 'c')],
		"DELTA" 					:	[('type', 'd')],
		"ECHO" 						:	[('type', 'e')],
		"FOXTROT" 					:	[('type', 'f')],
		"GOLF" 						:	[('type', 'g')],
		"HOTEL" 					:	[('type', 'h')],
		"INDIA" 					:	[('type', 'i')],
		"JULIETTE" 					:	[('type', 'j')],
		"KILO" 						:	[('type', 'k')],
		"LIMA" 						:	[('type', 'l')],
		"MIKE" 						:	[('type', 'm')],
		"NOVEMBER" 					:	[('type', 'n')],
		"OSCAR" 					:	[('type', 'o')],
		"PAPA" 						:	[('type', 'p')],
		"QUEBEC" 					:	[('type', 'q')],
		"ROMEO" 					:	[('type', 'r')],
		"SIERRA" 					:	[('type', 's')],
		"TANGO" 					:	[('type', 't')],
		"UNIFORM" 					:	[('type', 'u')],
		"VICTOR" 					:	[('type', 'v')],
		"WHISKEY" 					:	[('type', 'w')],
		"X-RAY" 					:	[('type', 'x')],
		"YANKEE" 					:	[('type', 'y')],
		"ZULU" 						:	[('type', 'z')],
		"CAP-ALPHA" 				:	[('type', 'A')],
		"CAP-BRAVO" 				:	[('type', 'B')],
		"CAP-CHARLIE" 				:	[('type', 'C')],
		"CAP-DELTA" 				:	[('type', 'D')],
		"CAP-ECHO" 					:	[('type', 'E')],
		"CAP-FOXTROT" 				:	[('type', 'F')],
		"CAP-GOLF" 					:	[('type', 'G')],
		"CAP-HOTEL" 				:	[('type', 'H')],
		"CAP-INDIA" 				:	[('type', 'I')],
		"CAP-JULIETTE" 				:	[('type', 'J')],
		"CAP-KILO" 					:	[('type', 'K')],
		"CAP-LIMA" 					:	[('type', 'L')],
		"CAP-MIKE" 					:	[('type', 'M')],
		"CAP-NOVEMBER" 				:	[('type', 'N')],
		"CAP-OSCAR" 				:	[('type', 'O')],
		"CAP-PAPA" 					:	[('type', 'P')],
		"CAP-QUEBEC" 				:	[('type', 'Q')],
		"CAP-ROMEO" 				:	[('type', 'R')],
		"CAP-SIERRA" 				:	[('type', 'S')],
		"CAP-TANGO" 				:	[('type', 'T')],
		"CAP-UNIFORM" 				:	[('type', 'U')],
		"CAP-VICTOR" 				:	[('type', 'V')],
		"CAP-WHISKEY" 				:	[('type', 'W')],
		"CAP-X-RAY" 				:	[('type', 'X')],
		"CAP-YANKEE" 				:	[('type', 'Y')],
		"CAP-ZULU" 					:	[('type', 'Z')]
	},

	'numbers' : {
		"ZERO" 						:	[('type', '0')],
		"ONE" 						:	[('type', '1')],
		"TWO" 						:	[('type', '2')],
		"THREE" 					:	[('type', '3')],
		"FOUR" 						:	[('type', '4')],
		"FIVE" 						:	[('type', '5')],
		"SIX" 						:	[('type', '6')],
		"SEVEN" 					:	[('type', '7')],
		"EIGHT" 					:	[('type', '8')],
		"NINE" 						:	[('type', '9')]
	},

	'golang' : {
		"BREAK" 					:	[('type', 'break')],
		"CASE" 						:	[('type', 'case')],
		"CHAN" 						:	[('type', 'chan')],
		"CONST" 					:	[('type', 'const')],
		"CONTINUE" 					:	[('type', 'continue')],
		"DEFAULT" 					:	[('type', 'default')],
		"DEFER" 					:	[('type', 'defer')],
		"ELSE" 						:	[('type', 'else')],
		"FALLTHROUGH" 				:	[('type', 'fallthrough')],
		"FOR" 						:	[('type', 'for')],
		"FUNC" 						:	[('type', 'func')],
		"GO" 						:	[('type', 'go')],
		"GOTO" 						:	[('type', 'goto')],
		"IF" 						:	[('type', 'if')],
		"IMPORT" 					:	[('type', 'import')],
		"INTERFACE" 				:	[('type', 'interface')],
		"MAP" 						:	[('type', 'map')],
		"PACKAGE" 					:	[('type', 'package')],
		"RANGE" 					:	[('type', 'range')],
		"RETURN" 					:	[('type', 'return')],
		"SELECT" 					:	[('type', 'select')],
		"STRUCT" 					:	[('type', 'struct')],
		"SWITCH" 					:	[('type', 'switch')],
		"TYPE" 						:	[('type', 'type')],
		"VAR" 						:	[('type', 'var')]
	}
}