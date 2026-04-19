#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct symtab
{
    char symbol[20];
    int address;
} sym[50];

struct littab
{
    char literal[20];
    int address;
} lit[50];

struct mot
{
    char mnemonic[20];
    int opcode;
} mot[5] = {
    {"MOVER",4},
    {"ADD",1},
    {"SUB",2},
    {"MOVEM",5},
    {"STOP",0}
};

int main()
{
    FILE *ic,*symf,*litf;
    int addr;
    char opcode[20],op1[20],op2[20];
    int symcount=0,litcount=0;
    int i,mc,operand;

    ic=fopen("intermediate.txt","r");
    symf=fopen("symtab.txt","r");
    litf=fopen("littab.txt","r");

    if(ic==NULL || symf==NULL || litf==NULL)
    {
        printf("File error");
        return 0;
    }

    while(fscanf(symf,"%s %d",sym[symcount].symbol,&sym[symcount].address)!=EOF)
        symcount++;

    while(fscanf(litf,"%s %d",lit[litcount].literal,&lit[litcount].address)!=EOF)
        litcount++;

    printf("\nOBJECT PROGRAM\n");

    while(fscanf(ic,"%d %s %s %s",&addr,opcode,op1,op2)!=EOF)
    {
        if(strcmp(opcode,"DS")==0)
        {
            printf("%d ----\n",addr);
            continue;
        }

        if(strcmp(opcode,"DC")==0)
        {
            printf("%d %s\n",addr,op1);
            continue;
        }

        if(strcmp(opcode,"STOP")==0)
        {
            printf("%d 00 0 000\n",addr);
            continue;
        }

        mc=-1;

        for(i=0;i<5;i++)
        {
            if(strcmp(mot[i].mnemonic,opcode)==0)
            {
                mc=mot[i].opcode;
                break;
            }
        }

        operand=0;

        for(i=0;i<symcount;i++)
        {
            if(strcmp(sym[i].symbol,op2)==0)
            {
                operand=sym[i].address;
                break;
            }
        }

        for(i=0;i<litcount;i++)
        {
            if(strcmp(lit[i].literal,op2)==0)
            {
                operand=lit[i].address;
                break;
            }
        }

        printf("%d %02d %s %03d\n",addr,mc,op1,operand);
    }

    fclose(ic);
    fclose(symf);
    fclose(litf);

    return 0;
}
