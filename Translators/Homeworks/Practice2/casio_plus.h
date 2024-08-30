typedef enum
{
    typeCon,
    typeId,
    typeOpr
} nodeEnum;

/* constants */
typedef struct
{
    nodeEnum type;
    int value; /* value of constant */
} conNodeType;

/* identifiers */
typedef struct
{
    nodeEnum type;
    char name[30];
} idNodeType;

/* operators */
typedef struct
{
    nodeEnum type;
    int oper;                 /* operator */
    int nops;                 /* number of operands */
    union nodeTypeTag *op[1]; /* operands (expandable) */
} oprNodeType;

typedef union nodeTypeTag
{
    nodeEnum type; /* type of node */
    conNodeType con; /* constants */
    idNodeType id;   /* identifiers */
    oprNodeType opr; /* operators */
} nodeType;

// extern std::map<std::string, int> sym;