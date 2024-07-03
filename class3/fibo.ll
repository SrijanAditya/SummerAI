; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"print"(i32 %".1")

define i32 @"fib"(i32 %"k")
{
alloca-lcfaljne:
  %"k.1" = alloca i32
  %"x" = alloca i32
  %"y" = alloca i32
  %"res1" = alloca i1
  %"res2" = alloca i1
  %"b" = alloca i32
  %"c" = alloca i32
  %"d" = alloca i32
  %"e" = alloca i32
  %"tmp1" = alloca i32
  %"tmp2" = alloca i32
  %"out" = alloca i32
  br label %"entry-kjqyxsxj"
entry-kjqyxsxj:
  store i32 %"k", i32* %"k.1"
  store i32 0, i32* %"x"
  store i32 1, i32* %"y"
  %".6" = load i32, i32* %"k.1"
  %".7" = load i32, i32* %"x"
  %"res1.1" = icmp eq i32 %".6", %".7"
  store i1 %"res1.1", i1* %"res1"
  %".9" = load i1, i1* %"res1"
  br i1 %".9", label %"zero", label %"other1"
zero:
  %".11" = load i32, i32* %"x"
  ret i32 %".11"
other1:
  %".13" = load i32, i32* %"k.1"
  %".14" = load i32, i32* %"y"
  %"res2.1" = icmp eq i32 %".13", %".14"
  store i1 %"res2.1", i1* %"res2"
  %".16" = load i1, i1* %"res2"
  br i1 %".16", label %"one", label %"other2"
one:
  %".18" = load i32, i32* %"y"
  ret i32 %".18"
other2:
  store i32 1, i32* %"b"
  store i32 2, i32* %"c"
  %".22" = load i32, i32* %"k.1"
  %".23" = load i32, i32* %"b"
  %"d.1" = sub i32 %".22", %".23"
  store i32 %"d.1", i32* %"d"
  %".25" = load i32, i32* %"k.1"
  %".26" = load i32, i32* %"c"
  %"e.1" = sub i32 %".25", %".26"
  store i32 %"e.1", i32* %"e"
  %".28" = load i32, i32* %"d"
  %"tmp1.1" = call i32 @"fib"(i32 %".28")
  store i32 %"tmp1.1", i32* %"tmp1"
  %".30" = load i32, i32* %"e"
  %"tmp2.1" = call i32 @"fib"(i32 %".30")
  store i32 %"tmp2.1", i32* %"tmp2"
  %".32" = load i32, i32* %"tmp1"
  %".33" = load i32, i32* %"tmp2"
  %"out.1" = add i32 %".32", %".33"
  store i32 %"out.1", i32* %"out"
  %".35" = load i32, i32* %"out"
  ret i32 %".35"
}

define i32 @"main"()
{
alloca-mxvckjgw:
  %"f" = alloca i32
  %"g" = alloca i32
  %"tmp" = alloca i32
  br label %"entry-rlqrczoa"
entry-rlqrczoa:
  store i32 5, i32* %"f"
  %".3" = load i32, i32* %"f"
  %"g.1" = call i32 @"fib"(i32 %".3")
  store i32 %"g.1", i32* %"g"
  %".5" = load i32, i32* %"g"
  %"tmp.1" = call i32 @"print"(i32 %".5")
  store i32 %"tmp.1", i32* %"tmp"
  %".7" = load i32, i32* %"tmp"
  ret i32 %".7"
}

