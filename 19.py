from inp import rules, msgs

msgs = msgs.split('\n')
rules = rules.split('\n')

print(msgs)
print(rules)


ruleDict = {}
 
invalidMessageDict = {}
 
for rule in rules:
        ruleParts = rule.split(": ")
        ruleName = ruleParts[0]
        options = [x.split(" ") for x in ruleParts[1].split(" | ")]
        ruleDict[ruleName] = options
 
def matchesRuleList(message, ruleList):
        if len(message) < len(ruleList):
                return False
        if len(message) == 0 and len(ruleList) == 0:
                return True
        if len(ruleList) == 0:
                return False
        for i in range(1, len(message) + 1):
                prefix = message[:i]
                firstRule = ruleList[0]
                if matchesRule(prefix, firstRule):
                        if matchesRuleList(message[i:], ruleList[1:]):
                                return True
        return False
 
def matchesRule(message, ruleName):
        if message in invalidMessageDict:
                if ruleName in invalidMessageDict[message]:
                        return False # If we already checked/saved this resut, return early
        options = ruleDict[ruleName]
        for option in options:
                if message in option:
                        return True
                if option[0] in ["a","b"]:
                        if message in invalidMessageDict:
                                invalidMessageDict[message].append(ruleName)
                        else:
                                invalidMessageDict[message] = []
                        return False
                if matchesRuleList(message, option):
                        return True
 
        if message in invalidMessageDict:
                invalidMessageDict[message].append(ruleName)
        else:
                invalidMessageDict[message] = []
        return False
 
       
 
print("Part 1:")
total = 0
for message in msgs:
        if matchesRule(message, "0"):
                total += 1
print(total)
 
 
 
print("Part 2:")
# Modify rules to create possible infinite loops
ruleDict["8"] = [["42"], ["42","8"]]
ruleDict["11"] = [["42","31"], ["42","11","31"]]
 
# Reset global variabels
invalidMessageDict = {}
total = 0
 
for message in msgs:
        if matchesRule(message, "0"):
                total += 1
print(total)