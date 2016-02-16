# FALCON-formatter
Even though it is more convenient to store all reads in a single FASTA or FASTQ file on your system, [Dazzler](https://github.com/thegenemyers/DAZZ_DB) (and therefore FALCON) does not accept this kind of input. All inputs **MUST** be in FASTA format with files split by barcode, set, and part number. This means that fields 1-6 in the example below must be unique to each input file.
```none
m140415_143853_42175_c100635972550000001823121909121417_s1_p0/553/3100_11230
1yymmdd_hhmmss 33333 4444444444444444444444444444444444 55 66 777 8888888888
```
1. “m” = movie
2. Time of Run Start (yymmdd_hhmmss)
3. Instrument Serial Number
4. SMRT Cell Barcode
5. Set Number
6. Part Number
7. ZMW hole number*
8. Subread Region (start_stop using polymerase read coordinates)*
* These fields are only used in fasta/q headers

More information can be found at the [SMRT-Analysis wiki](https://github.com/PacificBiosciences/SMRT-Analysis/wiki/Data-files-you-received-from-your-service-provider).

Below is an example that demonstrates this requirement and process by correctly splitting the file Example.fasta.

**Example.fasta**
```
>m140415_143853_42175_c100635972550000001823121909121417_s1_p0/553/3100_11230
>m140415_143853_42175_c324508543089230982134098587348034_s1_p0/553/103_725
>m140415_143853_42175_c324508543089230982134098587348034_s1_p0/553/973_13390
>m140415_143853_42175_c100635972550000001823121909121417_s1_p0/553/15030_17394
```

In the 4 headers, there are two unique 1-6 field sets:
```
>m140415_143853_42175_c100635972550000001823121909121417_s1_p0
>m140415_143853_42175_c324508543089230982134098587348034_s1_p0
```
All subreads corresponding to these headers need to be in their own files, so Example.fasta would be split accordingly:

**m140415_143853_42175_c100635972550000001823121909121417_s1_p0.fasta**
```
>m140415_143853_42175_c100635972550000001823121909121417_s1_p0/553/3100_11230
>m140415_143853_42175_c100635972550000001823121909121417_s1_p0/553/15030_17394
```
**m140415_143853_42175_c324508543089230982134098587348034_s1_p0.fasta**
```
>m140415_143853_42175_c324508543089230982134098587348034_s1_p0/553/103_725
>m140415_143853_42175_c324508543089230982134098587348034_s1_p0/553/973_13390
```
## Installation
Using setuptools
```
git clone https://github.com/zyndagj/FALCON-formatter
cd FALCON-formatter
python setup.py install --user
```
Using pip
```
pip install --user git+https://github.com/zyndagj/FALCON-formatter
```

## CLI Usage
The program FALCON-formatter (installed in `$HOME/.local/bin`) takes fastq and fasta files from a Pacific Biosciences sequencer and formats them for *de novo* assembly with [FALCON](https://github.com/PacificBiosciences/FALCON).

#### usage:
```
FALCON-formatter [-h] [-w INT] [-o STR] F [F ...]
```
#### positional arguments:
|Argument|Description|
|---|:---|
| F | Fastq/a files for folder for formatting |
#### optional arguments:
|Flag|Option|Description|
|---|---|:---|
|-h| |show this help message and exit|
|-w|INT|hard-wrap fasta output at \[80\] base-pairs|
|-o|DIR|output path \[.\]|

### Example
```
FALCON-formatter ecoli.fasta
Processing: ecoli.fasta
```

## CyVerse Usage
If you’re coming from Cyverse, you first need to find the FALCON-formatter app in the HPC app catalog and launch it. Then, click on the “Inputs” drop down arrow to designate your inputs.

![iplant_formatter_01](https://cloud.githubusercontent.com/assets/6790115/13088375/9e1a3c20-d4b1-11e5-8a43-a85ea903ddff.png)

Then, click the browse button to open up a file explorer to choose your input.

![iplant_formatter_02](https://cloud.githubusercontent.com/assets/6790115/13088373/9e18f126-d4b1-11e5-9118-33d83b679501.png)

Select either a single fastq/fastq file or a whole folder to process.

![iplant_formatter_03](https://cloud.githubusercontent.com/assets/6790115/13088374/9e1a41b6-d4b1-11e5-80db-2e4e2b025cd2.png)

Click “Launch Analysis” to start your job. You’ll get notifications when the program starts and when it finishes.

![iplant_formatter_04](https://cloud.githubusercontent.com/assets/6790115/13088376/9e1a9ac6-d4b1-11e5-936d-8486f4ba4174.png)
