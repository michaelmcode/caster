'''
Created November 2018

@author: Mike Roberts, Mike Morris 
'''
from dragonfly import Choice, Key, Text

from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.lib.ccr.standard import SymbolSpecs


class Go(MergeRule):

    mapping = {
        SymbolSpecs.IF:
            R(Text("if  {}") + Key("left, enter, up, end, left:2"), rdescript="Go: if"),
        SymbolSpecs.ELSE:
            R(Text("else {}") + Key("left, enter, up"), rdescript="Go: else"),
        #
        SymbolSpecs.SWITCH:
            R(Text("switch  {}") + Key("left, enter, up, end, left:2"),
              rdescript="Go: switch"),
        SymbolSpecs.CASE:
            R(Text("case :") + Key("left"), rdescript="Go: case"),
        SymbolSpecs.DEFAULT:
            R(Text("default:") + Key("enter"), rdescript="Go: default"),
        SymbolSpecs.BREAK:
            R(Text("break"), rdescript="Go: break"),
        #
        SymbolSpecs.WHILE_LOOP:
            R(Text("for  {}") + Key("left, enter, up, end, left:2"),
              rdescript="Go: while loop"),
        SymbolSpecs.FOR_LOOP:
            R(Text("for i := 0; i<; i++ {}") + Key("left, enter, up, end, left:7"),
              rdescript="Go: for loop"),
        SymbolSpecs.FOR_EACH_LOOP:
            R(Text("for  := range  {}") + Key("left, enter, up, home, right:4"),
              rdescript="Go: for each"),
        #
        SymbolSpecs.TO_INTEGER:
            R(Text("strconv.Atoi()") + Key("left"), rdescript="Go: convert to integer"),
        SymbolSpecs.TO_STRING:
            R(Text("strconv.Itoa()") + Key("left"), rdescript="Go: convert to string"),
        #
        SymbolSpecs.AND:
            R(Text(" && "), rdescript="Go: and"),
        SymbolSpecs.OR:
            R(Text(" || "), rdescript="Go: or"),
        SymbolSpecs.NOT:
            R(Text("!"), rdescript="Go: not"),
        #
        SymbolSpecs.SYSOUT:
            R(Text("fmt.Println()") + Key("left"), rdescript="Go: sysout"),
        #
        SymbolSpecs.IMPORT:
            R(Text("import ()") + Key("left, enter"), rdescript="Go: import"),
        #
        SymbolSpecs.FUNCTION:
            R(Text("func "), rdescript="Go: function"),
        SymbolSpecs.CLASS:
            R(Text("type  struct {}") + Key("left, enter, up, home, right:5"),
              rdescript="Go: class"),
        #
        SymbolSpecs.COMMENT:
            R(Text("//"), rdescript="Go: comment"),
        SymbolSpecs.LONG_COMMENT:
            R(Text("/**/") + Key("left, left"), rdescript="Go: long comment"),
        #
        SymbolSpecs.NULL:
            R(Text("nil"), rdescript="Go: nil"),
        #
        SymbolSpecs.RETURN:
            R(Text("return "), rdescript="Go: return"),
        #
        SymbolSpecs.TRUE:
            R(Text("true"), rdescript="Go: true"),
        SymbolSpecs.FALSE:
            R(Text("false"), rdescript="Go: false"),
        #
        "[type] (inter | integer)":
            R(Text("int"), rdescript="Go: integer"),
        "[type] boolean":
            R(Text("bool"), rdescript="Go: boolean"),
        "[type] string":
            R(Text("string"), rdescript="Go: string"),
        "assign":
            R(Text(" := "), rdescript="Go: assign"),
        "(function | funk) main":
            R(Text("func main() {}") + Key("left, enter"), rdescript="Go: main function"),
        "make map":
            R(Text("make(map[])") + Key("left:2"), rdescript="Go: create a map"),
        "package":
            R(Text("package "), rdescript="Go: package"),
        # Custom Updates
        "(end | finish) timer":
            R(Text("elapsed := time.Since(start)\nfmt.Printf(\"execution took %s\", elapsed)"), rdescript="Go: finish timer"),
        "(split string | strings split)":
            R(Text("strings.Split()") + Key("left"), rdescript="Go: split string"),
        "(start | begin) timer":
            R(Text("start := time.Now()"), rdescript="Go: split string"),
        "append":
            R(Text("") + Key("home/5, s-end, c-c, right, space, equal, space, a, p, p, e, n, d, lparen, c-v, comma, space"), rdescript="Go: append"),
        "create mutex":
            R(Text("var mutex = sync.Mutex{}"), rdescript="Go: create mutex"),
        "create weight group":
            R(Text("var wg sync.WaitGroup"), rdescript="Go: create weight group"),
        "go routine":
            R(Text("go "), rdescript="Go: go routing"),
        "make channel":
            R(Text("make(chan )") + Key("left"), rdescript="Go: make channel" ),
        "mutex lock":
            R(Text("mutex.Lock()"), rdescript="Go: mutex lock"),
        "mutex unlock":
            R(Text("mutex.Unlock()"), rdescript="Go: mutex unlock"),
        "package main":
            R(Text("package main") + Key("enter"), rdescript="Go: package main"),
        "file open":
            R(Text("file, _ := os.Open()\ndefer file.Close()") + Key("up, end, left, dquote"), rdescript="Go: file open"),
        "read file":
            R(Text("ioutil.ReadFile()") + Key("left, dquote"), rdescript="Go: read file"),
        "regular compile":
            R(Text("regexp.MustCompile()") + Key("left, dquote"), rdescript="Go: regular compile"),
        "regular find all [string] submatch":
            R(Text("FindAllStringSubmatch(, -1)") + Key("left:5"), rdescript="Go: regular find all submatch"),
        "scanner new":
            R(Text("scanner := bufio.NewScanner(file)"), rdescript="Go: scanner new"),
        "scanner scan":
            R(Text("scanner.Scan()"), rdescript="Go: scanner scan"),
        "scanner text":
            R(Text("scanner.Text()"), rdescript="Go: scanner text"),
        "send (message | channel)":
            R(Text(" <- "), rdescript="Go: send message or channel"),
        "shell iffae":
            R(Text("else if  {}") + Key("left:3"), rdescript="Go: shell iffae"),
        "variable":
            R(Text("var "), rdescript="Go: variable"),
        "weight group add":
            R(Text("wg.Add(1)"), rdescript="Go: weight group add"),
        "weight group done":
            R(Text("wg.Done()"), rdescript="Go: weight group done"),
        "weight group weight":
            R(Text("wg.Wait()"), rdescript="Go: weight group weight"),
        # Custom Types
        "(inter | integer) eight":
            R(Text("int8"), rdescript="Go: int8"),
        "(inter | integer) sixteen":
            R(Text("int16"), rdescript="Go: int16"),
        "(inter | integer) sixty four":
            R(Text("int64"), rdescript="Go: int64"),
        "(inter | integer) thirty two":
            R(Text("int32"), rdescript="Go: int32"),
        "(inter | integer)":
            R(Text("int"), rdescript="Go: int"),
        "boolean":
            R(Text("bool"), rdescript="Go: bool"),
        "byte":
            R(Text("byte"), rdescript="Go: byte"),
        "float":
            R(Text("float64"), rdescript="Go: float64"),
        "interface":
            R(Text("interface"), rdescript="Go: interface"),
        "rune":
            R(Text("rune"), rdescript="Go: rune"),
        "string":
            R(Text("string"), rdescript="Go: string"),
        "unsigned (inter | integer) eight":
            R(Text("uint8"), rdescript="Go: uint8"),
        "unsigned (inter | integer) sixteen":
            R(Text("uint16"), rdescript="Go: uint16"),
        "unsigned (inter | integer) sixty four":
            R(Text("uint64"), rdescript="Go: uint64"),
        "unsigned (inter | integer) thirty two":
            R(Text("uint32"), rdescript="Go: uint32"),
        "unsigned (inter | integer)":
            R(Text("uint"), rdescript="Go: uint"),
		"if error":
            R(Text("if err != nil {}") + Key("left"), rdescript="Go: if error"),
    }

    extras = []
    defaults = {}


control.nexus().merger.add_global_rule(Go())
