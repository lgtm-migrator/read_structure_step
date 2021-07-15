from read_structure_step.formats.registries import register_format_checker
from . import obabel  # noqa: F401

keywords = [
    "0SCF",
    "1ELECTRON",
    "1SCF",
    "ADD-H",
    "A0",
    "AIDER",
    "AIGIN",
    "AIGOUT",
    "ALLBONDS",
    "ALLVEC",
    "ALT_A=A",
    "ALT_R=A",
    "ANGSTROMS",
    "AUTOSYM",
    "AUX",
    "AM1",
    "BAR=n.nn",
    "BCC",
    "BIGCYCLES=n",
    "BIRADICAL",
    "BFGS",
    "BONDS",
    "CAMP",
    "CARTAB",
    "C.I.=n" "C.I.=(n,m)",
    "CHAINS(text)",
    "CHECK",
    "CHARGE=n",
    "CHARGES",
    "CHARST",
    "CIS",
    "CISD",
    "CISDT",
    "COMPARE",
    "COMPFG",
    "COSCCH",
    "COSWRT",
    "CUTOFP=n.nn",
    "CUTOFF=n.nn",
    "CYCLES=n",
    "CVB",
    "DAMP=n.nn",
    "DATA=text",
    "DCART",
    "DDMAX=n.nn",
    "DDMIN=n.nn",
    "DEBUG",
    "DEBUG PULAY",
    "DENOUT",
    "DENOUTF",
    "DENSITY",
    "DERI1",
    "DERI2",
    "DERITR",
    "DERIV",
    "DERNVO",
    "DFORCE",
    "DFP",
    "DISEX=n.nn",
    "DISP",
    "DMAX=n.nn",
    "DOUBLET",
    "DRC=n.nnn",
    "DUMP=nn.nn",
    "ECHO",
    "EF",
    "EIGEN",
    "EIGS",
    "ENPART",
    "EPS=n.nn",
    "ESP",
    "ESPRST",
    "ESR",
    "EXCITED",
    "EXTERNAL=name",
    "FIELD=(n.nn,m.mm,l.ll)",
    "FILL=n",
    "FLEPO",
    "FMAT",
    "FOCK",
    "FREQCY",
    "FORCE",
    "FORCETS",
    "GEO-OK",
    "GEO_DAT=<text>",
    "GEO_REF=<text>",
    "GNORM=n.nn",
    "GRADIENTS",
    "GRAPH",
    "GRAPHF",
    "HCORE",
    "HESSIAN",
    "HESS=n",
    "H-PRIORITY=n.nn",
    "HTML",
    "HYPERFINE",
    "INT",
    "INVERT",
    "IRC=n",
    "ISOTOPE",
    "ITER",
    "ITRY=nn",
    "IUPD=n",
    "KINETIC=n.nnn",
    "KING",
    "LARGE",
    "LBFGS",
    "LET",
    "LEWIS",
    "LINMIN",
    "LOCALIZE",
    "LOCATE-TS",
    "LOG",
    "MECI",
    "MERS=(n1,n2,n3)",
    "METAL=(a[,b[,c[...]]])",
    "MICROS=n",
    "MINI",
    "MINMEP",
    "MMOK",
    "MNDO",
    "MNDOD",
    "MODE=n",
    "MOL_QMMM",
    "MOLDAT",
    "MOLSYM",
    "MOPAC",
    "MOZYME",
    "MS=n",
    "MULLIK",
    "N**2=n.nn",
    "NLLSQ",
    "NOANCI",
    "NOCOMMENTS",
    "NOGPU",
    "NOLOG",
    "NOMM",
    "NONET",
    "NONR",
    "NOOPT",
    "NOOPT-X",
    "NOREOR",
    "NORESEQ",
    "NOSWAP",
    "NOSYM",
    "NOTER",
    "NOTHIEL",
    "NOTXT",
    "NOXYZ",
    "NSPA=n",
    "NSURF",
    "OCTET",
    "OLDCAV",
    "OLDENS",
    "OLDFPC",
    "OLDGEO",
    "OMIN=n.nn",
    "OPEN(n1,n2)",
    "OPT",
    "OPT-X",
    "OPT(text=n.nn)",
    "OUTPUT",
    "P=n.nn",
    "PDB",
    "PDB=(text)",
    "PDBOUT	",
    "PECI",
    "PI",
    "pKa",
    "PL",
    "PM3",
    "PM6",
    "PM6-D3",
    "PM6-DH+",
    "PM6-DH2",
    "PM6-DH2X",
    "PM6-D3H4",
    "PM6-D3H4X",
    "PMEP",
    "PM7",
    "PM7-TS",
    "PMEPR",
    "POINT=n",
    "POINT1=n",
    "POINT2=n",
    "POLAR",
    "POTWRT",
    "POWSQ",
    "PRECISE",
    "PRESSURE",
    "PRNT=n",
    "PRTCHAR",
    "PRTINT",
    "PRTMEP",
    "PRTXYZ",
    "PULAY",
    "QMMM",
    "QPMEP",
    "QUARTET",
    "QUINTET",
    "RAPID",
    "RECALC=n",
    "RE-LOCAL",
    "RE-LOCAL=n",
    "RELSCF",
    "REORTHOG",
    "RESEQ",
    "RESIDUES",
    "RESTART",
    "RHF",
    "RM1",
    "RMAX=n.nn",
    "RMIN=n.nn",
    "ROOT=n",
    "RSCAL",
    "RSOLV=n.nn",
    "SADDLE",
    "SCALE",
    "SCFCRT=n.nn",
    "SCINCR=n.nn",
    "SEPTET",
    "SETPI",
    "SETUP",
    "SEXTET",
    "SHIFT=n.nn",
    #'SHUT <file>', # noqa: E265
    "SIGMA",
    "SINGLET",
    "SITE=(text)",
    "SLOG=n.nn",
    "SLOPE",
    "SMOOTH",
    "SNAP",
    "SPARKLE",
    "SPIN",
    "START_RES(text)",
    "STATIC",
    "STEP",
    "STEP1=n.nnn",
    "STEP2=n.nnn",
    "STO3G",
    "SUPER",
    "SYBYL",
    "SYMAVG",
    "SYMOIR",
    "SYMTRZ",
    "SYMMETRY",
    "T=n[M,H,D]",
    "THERMO(nnn,mmm,lll)",
    "THREADS=n",
    "TIMES",
    "T-PRIORITY=n.nn",
    "TRANS=n",
    "TRIPLET",
    "TS",
    "UHF",
    "VDW(text)",
    "VDWM(text)",
    "VECTORS",
    "VELOCITY",
    "WILLIAMS",
    "X-PRIORITY=n.nn",
    "XENO",
    "XYZ",
    "Z=n",
]


@register_format_checker(".mop")
def check_format(file_name):

    with open(file_name, "r") as f:

        data = f.read()

        if any(keyword in data for keyword in keywords):
            return True
        else:
            return False
