#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct symtab
{
    char symbol[10];
    int address;
}sym[50];

struct littab
{
    char literal[10];
    int address;
}lit[50];

int main()
{
    FILE *fp;
    char label[20], opcode[20], op1[20], op2[20];
    int lc=0,start=0;
    int symcount=0,litcount=0;
    int i;

    printf("\nMACHINE OPERATION TABLE (MOT)\n");
    printf("MOVER\nADD\nSUB\nMOVEM\nSTOP\n");

    printf("\nPSEUDO OPERATION TABLE (POT)\n");
    printf("START\nEND\nDS\nDC\n");

    fp=fopen("input.asm","r");

    if(fp==NULL)
    {
        printf("File not found\n");
        return 0;
    }

    printf("\nINTERMEDIATE CODE\n");

    while(fscanf(fp,"%s %s %s %s",label,opcode,op1,op2)!=EOF)
    {

        if(strcmp(label,"START")==0)
        {
            lc=atoi(opcode);
            start=lc;
            printf("(AD,01) (C,%d)\n",lc);
            continue;
        }

        if(strcmp(label,"END")==0)
        {
            printf("(AD,02)\n");
            break;
        }

        if(strcmp(label,"-")!=0)
        {
            strcpy(sym[symcount].symbol,label);
            sym[symcount].address=lc;
            symcount++;
        }

        if(op2[0]=='=')
        {
            int found=0;

            for(i=0;i<litcount;i++)
            {
                if(strcmp(lit[i].literal,op2)==0)
                {
                    found=1;
                    break;
                }
            }

            if(!found)
            {
                strcpy(lit[litcount].literal,op2);
                lit[litcount].address=-1;
                litcount++;
            }
        }

        if(strcmp(opcode,"DS")==0)
        {
            printf("%d (DL) DS %s\n",lc,op1);
            lc+=atoi(op1);
        }

        else if(strcmp(opcode,"DC")==0)
        {
            printf("%d (DL) DC %s\n",lc,op1);
            lc++;
        }

        else if(strcmp(opcode,"STOP")==0)
        {
            printf("%d (IS) STOP\n",lc);
            lc++;
        }

        else
        {
            printf("%d (IS) %s %s %s\n",lc,opcode,op1,op2);
            lc++;
        }

    }

    fclose(fp);

    int program_length = lc - start;

    for(i=0;i<litcount;i++)
    {
        lit[i].address = lc;
        lc++;
    }

    printf("\nPROGRAM LENGTH\n");
    printf("%d\n",program_length);

    printf("\nSYMBOL TABLE\n");

    for(i=0;i<symcount;i++)
    {
        printf("%s\t%d\n",sym[i].symbol,sym[i].address);
    }

    printf("\nLITERAL TABLE\n");

    for(i=0;i<litcount;i++)
    {
        printf("%s\t%d\n",lit[i].literal,lit[i].address);
    }

    printf("\nBASE TABLE (BT)\n");
    printf("Base Register\tContent\n");
    printf("BR\t%d\n",start);

    return 0;
}