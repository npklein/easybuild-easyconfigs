exts_list = [
    ('lattice', '0.20-35', cran_options),
    ('nlme', '3.1-131.1', cran_options),
    ('Matrix', '1.2-12', cran_options),
    ('mgcv', '1.8-26', cran_options),
    ('plotfunctions', '1.3', cran_options),
    ('itsadug', '2.3', cran_options),
    ('abind', '1.4-5', cran_options),
    ('acepack', '1.4.1', cran_options),
    ('MASS', '7.3-49', cran_options),
    ('ade4', '1.7-10', cran_options),
    ('tkrplot', '0.0-23', cran_options),
    ('foreign', '0.8-69', cran_options),
    ('shapefiles', '0.7', cran_options),
    ('sp', '1.2-7', cran_options),
    ('adehabitat', '1.8.20', cran_options),
    ('nnet', '7.3-12', cran_options),
    ('Rcpp', '0.12.16', cran_options),
    ('minqa', '1.2.4', cran_options),
    ('nloptr', '1.0.4', cran_options),
    ('RcppEigen', '0.3.3.4.0', cran_options),
    ('lme4', '1.1-15', cran_options),
    ('pbkrtest', '0.4-7', cran_options),
    ('SparseM', '1.77', cran_options),
    ('MatrixModels', '0.4-1', cran_options),
    ('quantreg', '5.35', cran_options),
    ('car', '2.1-6', cran_options),
    ('zoo', '1.8-1', cran_options),
    ('lmtest', '0.9-35', cran_options),
    ('sandwich', '2.4-0', cran_options),
    ('survival', '2.41-3', cran_options),
    ('Formula', '1.2-2', cran_options),
    ('AER', '1.2-5', cran_options),
    ('combinat', '0.0-8', cran_options),
    ('httpuv', '1.3.6.2', cran_options),
    ('mime', '0.5', cran_options),
    ('jsonlite', '1.5', cran_options),
    ('xtable', '1.8-2', cran_options),
    ('digest', '0.6.15', cran_options),
    ('htmltools', '0.3.6', cran_options),
    ('R6', '2.2.2', cran_options),
    ('sourcetools', '0.1.6', cran_options),
    ('shiny', '1.0.5', cran_options),
    ('miniUI', '0.1.1', cran_options),
    ('rstudioapi', '0.7', cran_options),
    ('highr', '0.6', cran_options),
    ('class', '7.3-14', cran_options),
    ('e1071', '1.6-8', cran_options),
    ('classInt', '0.1-24', cran_options),
    ('magrittr', '1.5', cran_options),
    ('rlang', '0.2.0', cran_options),
    ('assertthat', '0.2.0', cran_options),
    ('crayon', '1.3.4', cran_options),
    ('cli', '1.0.0', cran_options),
    ('utf8', '1.1.3', cran_options),
    ('pillar', '1.2.1', cran_options),
    ('tibble', '1.4.2', cran_options),
    ('forcats', '0.3.0', cran_options),
    ('pkgconfig', '2.0.1', cran_options),
    ('hms', '0.4.2', cran_options),
    ('BH', '1.66.0-1', cran_options),
    ('readr', '1.1.1', cran_options),
    ('haven', '1.1.1', cran_options),
    ('labelled', '1.0.1', cran_options),
    ('questionr', '0.6.2', cran_options),
    ('klaR', '0.6-14', cran_options),
    ('cluster', '2.0.6', cran_options),
    ('spData', '0.2.8.3', cran_options),
    ('LearnBayes', '2.15.1', cran_options),
    ('deldir', '0.1-14', cran_options),
    ('boot', '1.3-20', cran_options),
    ('coda', '0.19-1', cran_options),
    ('gtools', '3.5.0', cran_options),
    ('gdata', '2.18.0', cran_options),
    ('gmodels', '2.16.2', cran_options),
    ('expm', '0.999-2', cran_options),
    ('spdep', '0.7-4', cran_options),
    ('AlgDesign', '1.1-7.3', cran_options),
    ('agricolae', '1.2-8', cran_options),
    ('akima', '0.6-2', cran_options),
    ('animation', '2.5', cran_options),
    ('BiocGenerics', '0.24.0', bioconductor_options),
    ('Biobase', '2.38.0', bioconductor_options),
    ('S4Vectors', '0.16.0', bioconductor_options),
    ('IRanges', '2.12.0', bioconductor_options),
    ('DBI', '0.8', cran_options),
    ('bit', '1.1-12', cran_options),
    ('bit64', '0.9-7', cran_options),
    ('prettyunits', '1.0.2', cran_options),
    ('blob', '1.1.1', cran_options),
    ('memoise', '1.1.0', cran_options),
    ('plogr', '0.2.0', cran_options),
    ('RSQLite', '2.0', cran_options),
    ('AnnotationDbi', '1.40.0', bioconductor_options),
    ('XML', '3.98-1.10', cran_options),
    ('bitops', '1.0-6', cran_options),
    ('RCurl', '1.95-4.10', cran_options),
    ('annotate', '1.56.2', bioconductor_options),
    ('ape', '5.0', cran_options),
    ('proto', '1.0.0', cran_options),
    ('findpython', '1.0.3', cran_options),
    ('getopt', '1.20.2', cran_options),
    ('argparse', '1.1.1', cran_options),
    ('argparser', '0.4', cran_options),
    ('arm', '1.9-3', cran_options),
    ('AUC', '0.3.0', cran_options),
    ('backports', '1.1.2', cran_options),
    ('openssl', '1.0.1', cran_options),
    ('base64', '2.0', cran_options),
    ('base64enc', '0.1-3', cran_options),
    ('bindr', '0.1.1', cran_options),
    ('bindrcpp', '0.2', cran_options),
    ('glue', '1.2.0', cran_options),
    ('dplyr', '0.7.4', cran_options),
    ('gtable', '0.2.0', cran_options),
    ('plyr', '1.8.4', cran_options),
    ('stringi', '1.1.7', cran_options),
    ('stringr', '1.3.0', cran_options),
    ('reshape2', '1.4.3', cran_options),
    ('RColorBrewer', '1.1-2', cran_options),
    ('dichromat', '2.0-0', cran_options),
    ('colorspace', '1.3-2', cran_options),
    ('munsell', '0.4.3', cran_options),
    ('labeling', '0.3', cran_options),
    ('viridisLite', '0.3.0', cran_options),
    ('scales', '0.5.0', cran_options),
    ('lazyeval', '0.2.1', cran_options),
    ('ggplot2', '2.2.1', cran_options),
    ('bayesplot', '1.4.0', cran_options),
    ('numDeriv', '2016.8-1', cran_options),
    ('bbmle', '1.0.20', cran_options),
    ('bdsmatrix', '1.3-3', cran_options),
    ('beanplot', '1.2', cran_options),
    ('beeswarm', '0.2.3', cran_options),
    ('modeltools', '0.2-21', cran_options),
    ('flexmix', '2.3-14', cran_options),
    ('betareg', '3.1-0', cran_options),
    ('bibtex', '0.4.2', cran_options),
    ('biglm', '0.9-1', cran_options),
    ('bigmemory.sri', '0.1.3', cran_options),
    ('bigmemory', '4.5.33', cran_options),
    ('hglm.data', '1.0-0', cran_options),
    ('hglm', '2.1-1', cran_options),
    ('DatABEL', '0.9-6', cran_options),
    ('bigRR', '1.3-10', cran_options),
    ('gmp', '0.5-13.1', cran_options),
    ('polynom', '1.3-9', cran_options),
    ('partitions', '1.9-19', cran_options),
    ('binGroup', '2.1-1', cran_options),
    ('rappdirs', '0.3.1', cran_options),
    ('yaml', '2.1.18', cran_options),
    ('curl', '3.1', cran_options),
    ('httr', '1.3.1', cran_options),
    ('xml2', '1.2.0', cran_options),
    ('semver', '0.2.0', cran_options),
    ('binman', '0.1.0', cran_options),
    ('BiocInstaller', '1.28.0', bioconductor_options),
    ('lambda.r', '1.2', cran_options),
    ('futile.options', '1.0.0', cran_options),
    ('futile.logger', '1.4.3', cran_options),
    ('snow', '0.4-2', cran_options),
    ('BiocParallel', '1.12.0', bioconductor_options),
    ('progress', '1.1.2', cran_options),
    ('biomaRt', '2.34.2', bioconductor_options),
    ('zlibbioc', '1.24.0', bioconductor_options),
    ('rhdf5', '2.22.0', bioconductor_options),
    ('biomformat', '1.6.0', bioconductor_options),
    ('XVector', '0.18.0', bioconductor_options),
    ('Biostrings', '2.46.0', bioconductor_options),
    ('evaluate', '0.10.1', cran_options),
    ('markdown', '0.8', cran_options),
    ('knitr', '1.20', cran_options),
    ('rprojroot', '1.3-2', cran_options),
    ('rmarkdown', '1.9', cran_options),
    ('xfun', '0.1', cran_options),
    ('tinytex', '0.4', cran_options),
    ('bookdown', '0.7', cran_options),
    ('profileModel', '0.5-9', cran_options),
    ('brglm', '0.6.1', cran_options),
    ('qvcalc', '0.9-1', cran_options),
    ('BradleyTerry2', '1.0-8', cran_options),
    ('brew', '1.0-6', cran_options),
    ('mvtnorm', '1.0-7', cran_options),
    ('Brobdingnag', '1.2-5', cran_options),
    ('bridgesampling', '0.4-0', cran_options),
    ('StanHeaders', '2.17.2', cran_options),
    ('inline', '0.3.14', cran_options),
    ('gridExtra', '2.3', cran_options),
    ('rstan', '2.17.3', cran_options),
    ('matrixStats', '0.53.1', cran_options),
    ('loo', '1.1.0', cran_options),
    ('rstantools', '1.4.0', cran_options),
    ('htmlwidgets', '1.0', cran_options),
    ('shinyjs', '1.0', cran_options),
    ('colourpicker', '1.0', cran_options),
    ('crosstalk', '1.0.0', cran_options),
    ('DT', '0.4', cran_options),
    ('xts', '0.10-2', cran_options),
    ('dygraphs', '1.1.1.4', cran_options),
    ('PKI', '0.1-5.1', cran_options),
    ('RJSONIO', '1.3-0', cran_options),
    ('packrat', '0.4.9-1', cran_options),
    ('rsconnect', '0.8.8', cran_options),
    ('shinythemes', '1.1.1', cran_options),
    ('igraph', '1.2.1', cran_options),
    ('threejs', '0.3.1', cran_options),
    ('shinystan', '2.4.0', cran_options),
    ('nleqslv', '3.3.1', cran_options),
    ('brms', '2.1.0', cran_options),
    ('purrr', '0.2.4', cran_options),
    ('tidyselect', '0.2.4', cran_options),
    ('tidyr', '0.8.0', cran_options),
    ('mnormt', '1.5-5', cran_options),
    ('psych', '1.7.8', cran_options),
    ('broom', '0.4.3', cran_options),
    ('GenomeInfoDbData', '1.0.0', bioconductor_options),
    ('GenomeInfoDb', '1.14.0', bioconductor_options),
    ('GenomicRanges', '1.30.3', bioconductor_options),
    ('Rsamtools', '1.30.0', bioconductor_options),
    ('DelayedArray', '0.4.1', bioconductor_options),
    ('SummarizedExperiment', '1.8.1', bioconductor_options),
    ('GenomicAlignments', '1.14.1', bioconductor_options),
    ('rtracklayer', '1.38.3', bioconductor_options),
    ('BSgenome', '1.46.0', bioconductor_options),
    ('BSgenome.Hsapiens.UCSC.hg19', '1.4.0', bioconductor_options),
    ('statnet.common', '4.0.0', cran_options),
    ('network', '1.13.0', cran_options),
    ('DEoptimR', '1.0-8', cran_options),
    ('robustbase', '0.92-8', cran_options),
    ('trust', '0.1-7', cran_options),
    ('lpSolve', '5.6.13', cran_options),
    ('ergm', '3.8.0', cran_options),
    ('xergm.common', '1.7.7', cran_options),
    ('networkDynamic', '0.9.0', cran_options),
    ('tergm', '3.4.1', cran_options),
    ('ergm.count', '3.2.2', cran_options),
    ('sna', '2.4', cran_options),
    ('statnet', '2016.9', cran_options),
    ('texreg', '1.36.23', cran_options),
    ('caTools', '1.17.1', cran_options),
    ('KernSmooth', '2.23-15', cran_options),
    ('gplots', '3.0.1', cran_options),
    ('ROCR', '1.0-7', cran_options),
    ('speedglm', '0.3-2', cran_options),
    ('RSiena', '1.2-3', cran_options),
    ('btergm', '1.9.1', cran_options),
    ('codetools', '0.2-15', cran_options),
    ('iterators', '1.0.9', cran_options),
    ('foreach', '1.4.4', cran_options),
    ('locfit', '1.5-9.1', cran_options),
    ('limma', '3.34.9', bioconductor_options),
    ('registry', '0.5', cran_options),
    ('pkgmaker', '0.22', cran_options),
    ('rngtools', '1.2.4', cran_options),
    ('doRNG', '1.6.6', cran_options),
    ('RMySQL', '0.10.14', cran_options),
    ('GenomicFeatures', '1.30.3', bioconductor_options),
    ('bumphunter', '1.20.0', bioconductor_options),
    ('ca', '0.70', cran_options),
    ('Cairo', '1.5-9', cran_options),
    ('debugme', '1.1.0', cran_options),
    ('praise', '1.0.0', cran_options),
    ('withr', '2.1.2', cran_options),
    ('testthat', '2.0.0', cran_options),
    ('callr', '2.0.2', cran_options),
    ('CARBayesdata', '2.0', cran_options),
    ('matrixcalc', '1.0-3', cran_options),
    ('mcmc', '0.9-5', cran_options),
    ('MCMCpack', '1.4-2', cran_options),
    ('dotCall64', '0.9-5.2', cran_options),
    ('spam', '2.1-2', cran_options),
    ('truncnorm', '1.0-8', cran_options),
    ('CARBayes', '5.0', cran_options),
    ('carData', '3.0-0', cran_options),
    ('ModelMetrics', '1.1.0', cran_options),
    ('rpart', '4.1-13', cran_options),
    ('SQUAREM', '2017.10-1', cran_options),
    ('lava', '1.6', cran_options),
    ('prodlim', '1.6.1', cran_options),
    ('ipred', '0.9-6', cran_options),
    ('kernlab', '0.9-25', cran_options),
    ('CVST', '0.2-1', cran_options),
    ('DRR', '0.0.3', cran_options),
    ('dimRed', '0.1.0', cran_options),
    ('lubridate', '1.7.3', cran_options),
    ('timeDate', '3043.102', cran_options),
    ('sfsmisc', '1.1-2', cran_options),
    ('ddalpha', '1.3.1.1', cran_options),
    ('gower', '0.1.2', cran_options),
    ('RcppRoll', '0.2.2', cran_options),
    ('recipes', '0.1.2', cran_options),
    ('caret', '6.0-78', cran_options),
    ('proxy', '0.4-21', cran_options),
    ('cba', '0.2-19', cran_options),
    ('rematch', '1.0.1', cran_options),
    ('cellranger', '1.1.0', cran_options),
    ('changepoint', '2.2.2', cran_options),
    ('checkmate', '1.8.5', cran_options),
    ('pcaPP', '1.9-73', cran_options),
    ('som', '0.3-5.1', cran_options),
    ('lars', '1.2', cran_options),
    ('pls', '2.6-0', cran_options),
    ('mclust', '5.4', cran_options),
    ('chemometrics', '1.4.2', cran_options),
    ('chron', '2.3-52', cran_options),
    ('CircStats', '0.2-4', cran_options),
    ('circular', '0.4-93', cran_options),
    ('clubSandwich', '0.3.0', cran_options),
    ('miscTools', '0.6-22', cran_options),
    ('maxLik', '1.3-4', cran_options),
    ('plm', '1.6-6', cran_options),
    ('statmod', '1.4.30', cran_options),
    ('mlogit', '0.2-4', cran_options),
    ('clusterSEs', '2.4.1', cran_options),
    ('cmprsk', '2.2-7', cran_options),
    ('CODEX', '1.10.0', bioconductor_options),
    ('TH.data', '1.0-8', cran_options),
    ('multcomp', '1.4-8', cran_options),
    ('coin', '1.2-2', cran_options),
    ('commonmark', '1.4', cran_options),
    ('corpcor', '1.6.9', cran_options),
    ('rex', '1.1.2', cran_options),
    ('covr', '3.0.1', cran_options),
    ('cowplot', '0.9.2', cran_options),
    ('coxme', '2.2-7', cran_options),
    ('cubature', '1.3-11', cran_options),
    ('Cubist', '0.2.1', cran_options),
    ('data.table', '1.10.4-3', cran_options),
    ('dbplyr', '1.2.1', cran_options),
    ('prabclus', '2.2-6', cran_options),
    ('diptest', '0.75-7', cran_options),
    ('trimcluster', '0.1-2', cran_options),
    ('fpc', '2.1-11', cran_options),
    ('whisker', '0.3-2', cran_options),
    ('viridis', '0.5.0', cran_options),
    ('dendextend', '1.7.0', cran_options),
    ('desc', '1.1.1', cran_options),
    ('genefilter', '1.60.0', bioconductor_options),
    ('geneplotter', '1.56.0', bioconductor_options),
    ('latticeExtra', '0.6-28', cran_options),
    ('htmlTable', '1.11.2', cran_options),
    ('Hmisc', '4.1-1', cran_options),
    ('RcppArmadillo', '0.8.400.0.0', cran_options),
    ('DESeq2', '1.18.1', bioconductor_options),
    ('deSolve', '1.20', cran_options),
    ('git2r', '0.21.0', cran_options),
    ('devtools', '1.13.5', cran_options),
    ('shape', '1.4.4', cran_options),
    ('diagram', '1.6.4', cran_options),
    ('scatterplot3d', '0.3-41', cran_options),
    ('diffusionMap', '1.1-0', cran_options),
    ('dlm', '1.1-4', cran_options),
    ('DNAcopy', '1.52.0', bioconductor_options),
    ('doParallel', '1.0.11', cran_options),
    ('doSNOW', '1.0.16', cran_options),
    ('downloader', '0.4', cran_options),
    ('dtplyr', '0.0.2', cran_options),
    ('dtw', '1.18-1', cran_options),
    ('dynlm', '0.3-5', cran_options),
    ('plotrix', '3.7', cran_options),
    ('TeachingDemos', '2.10', cran_options),
    ('plotmo', '3.3.6', cran_options),
    ('fda', '2.4.7', cran_options),
    ('tis', '1.34', cran_options),
    ('jpeg', '0.1-8', cran_options),
    ('Ecfun', '0.1-7', cran_options),
    ('Ecdat', '0.3-1', cran_options),
    ('edgeR', '3.20.9', bioconductor_options),
    ('survey', '3.33-2', cran_options),
    ('effects', '4.0-0', cran_options),
    ('eha', '2.5.1', cran_options),
    ('ellipse', '0.4.1', cran_options),
    ('estimability', '1.3', cran_options),
    ('emmeans', '1.1.2', cran_options),
    ('epitools', '0.5-10', cran_options),
    ('quadprog', '1.5-5', cran_options),
    ('TTR', '0.23-3', cran_options),
    ('quantmod', '0.4-12', cran_options),
    ('tseries', '0.10-43', cran_options),
    ('fracdiff', '1.4-2', cran_options),
    ('forecast', '8.2', cran_options),
    ('expsmooth', '2.3', cran_options),
    ('fansi', '0.4.0', cran_options),
    ('fastcluster', '1.1.24', cran_options),
    ('fastICA', '1.2-1', cran_options),
    ('fastmatch', '1.1-0', cran_options),
    ('timeSeries', '3042.102', cran_options),
    ('spatial', '7.3-11', cran_options),
    ('gss', '2.1-7', cran_options),
    ('stabledist', '0.7-1', cran_options),
    ('fBasics', '3042.89', cran_options),
    ('ff', '2.2-13', cran_options),
    ('ffbase', '0.12.3', cran_options),
    ('fGarch', '3042.83', cran_options),
    ('filehash', '2.4-1', cran_options),
    ('fit.models', '0.5-14', cran_options),
    ('fitdistrplus', '1.0-9', cran_options),
    ('mstate', '0.2.10', cran_options),
    ('muhaz', '1.2.6', cran_options),
    ('flexsurv', '1.1', cran_options),
    ('FMStable', '0.1-2', cran_options),
    ('FNN', '1.1', cran_options),
    ('fontBitstreamVera', '0.1.1', cran_options),
    ('fontLiberation', '0.1.0', cran_options),
    ('fontquiver', '0.2.1', cran_options),
    ('formatR', '1.5', cran_options),
    ('fTrading', '3042.79', cran_options),
    ('gam', '1.15', cran_options),
    ('gamlss.data', '5.0-0', cran_options),
    ('gamlss.dist', '5.0-4', cran_options),
    ('gamlss', '5.0-6', cran_options),
    ('gapminder', '0.3.0', cran_options),
    ('gbm', '2.1.3', cran_options),
    ('gdtools', '0.1.7', cran_options),
    ('gee', '4.13-19', cran_options),
    ('geepack', '1.2-1', cran_options),
    ('GenABEL.data', '1.0.0', cran_options),
    ('GenABEL', '1.8-0', cran_options),
    ('genetics', '1.3.8.1', cran_options),
    ('magic', '1.5-8', cran_options),
    ('geometry', '0.3-6', cran_options),
    ('GEOquery', '2.46.15', bioconductor_options),
    ('geosphere', '1.5-7', cran_options),
    ('permute', '0.9-4', cran_options),
    ('vegan', '2.4-6', cran_options),
    ('RcppParallel', '4.4.0', cran_options),
    ('slackr', '1.4.2', cran_options),
    ('GERGM', '0.11.2', cran_options),
    ('getPass', '0.2-2', cran_options),
    ('reshape', '0.8.7', cran_options),
    ('GGally', '1.3.2', cran_options),
    ('vipor', '0.4.5', cran_options),
    ('ggbeeswarm', '0.6.0', cran_options),
    ('ggfortify', '0.4.3', cran_options),
    ('ggplot2movies', '0.0.1', cran_options),
    ('ggrepel', '0.7.0', cran_options),
    ('ggridges', '0.4.1', cran_options),
    ('ggthemes', '3.4.0', cran_options),
    ('glmnet', '2.0-13', cran_options),
    ('gmailr', '0.7.1', cran_options),
    ('gmm', '1.6-2', cran_options),
    ('relimp', '1.0-5', cran_options),
    ('gnm', '1.0-8', cran_options),
    ('goftest', '1.1-1', cran_options),
    ('googleVis', '0.6.2', cran_options),
    ('gridBase', '0.4-7', cran_options),
    ('gridSVG', '1.6-0', cran_options),
    ('grImport', '0.9-0', cran_options),
    ('grr', '0.9.5', cran_options),
    ('gsalib', '2.1', cran_options),
    ('gWidgets', '0.0-54', cran_options),
    ('polspline', '1.1.12', cran_options),
    ('rms', '5.1-2', cran_options),
    ('haplo.stats', '1.7.7', cran_options),
    ('heatmap3', '1.1.1', cran_options),
    ('hexbin', '1.27.2', cran_options),
    ('HSAUR', '1.3-9', cran_options),
    ('HSAUR3', '1.0-8', cran_options),
    ('hunspell', '2.9', cran_options),
    ('hwriter', '1.3.2', cran_options),
    ('ibdreg', '0.2.5', cran_options),
    ('ica', '1.0-1', cran_options),
    ('igraphdata', '1.0.1', cran_options),
    ('nor1mix', '1.2-3', cran_options),
    ('multtest', '2.34.0', bioconductor_options),
    ('siggenes', '1.52.0', bioconductor_options),
    ('preprocessCore', '1.40.0', bioconductor_options),
    ('illuminaio', '0.20.0', bioconductor_options),
    ('minfi', '1.24.0', bioconductor_options),
    ('IlluminaHumanMethylationEPICanno.ilm10b2.hg19', '0.6.0', bioconductor_options),
    ('IlluminaHumanMethylationEPICanno.ilm10b4.hg19', '0.6.0', bioconductor_options),
    ('IlluminaHumanMethylationEPICmanifest', '0.3.0', bioconductor_options),
    ('inlinedocs', '2013.9.3', cran_options),
    ('repr', '0.12.0', cran_options),
    ('IRdisplay', '0.4.4', cran_options),
    ('irlba', '2.3.2', cran_options),
    ('Iso', '0.0-17', cran_options),
    ('ISwR', '2.0-7', cran_options),
    ('jose', '0.1', cran_options),
    ('JuliaCall', '0.12.1', cran_options),
    ('KFAS', '1.3.1', cran_options),
    ('misc3d', '0.8-4', cran_options),
    ('multicool', '0.1-10', cran_options),
    ('plot3D', '1.1.1', cran_options),
    ('rgl', '0.99.9', cran_options),
    ('plot3Drgl', '1.0.1', cran_options),
    ('OceanView', '1.0.4', cran_options),
    ('ks', '1.11.0', cran_options),
    ('Lahman', '6.0-0', cran_options),
    ('png', '0.1-7', cran_options),
    ('raster', '2.6-7', cran_options),
    ('leaflet', '1.1.0', cran_options),
    ('RSpectra', '0.12-0', cran_options),
    ('rARPACK', '0.11-0', cran_options),
    ('lfda', '1.1.2', cran_options),
    ('lfe', '2.6-2291', cran_options),
    ('stringdist', '0.9.4.7', cran_options),
    ('lintr', '1.0.2', cran_options),
    ('listviewer', '2.0.0', cran_options),
    ('lmerTest', '2.0-36', cran_options),
    ('lmodel2', '1.7-3', cran_options),
    ('logging', '0.7-103', cran_options),
    ('logspline', '2.1.9', cran_options),
    ('longmemo', '1.0-0', cran_options),
    ('lsmeans', '2.27-61', cran_options),
    ('mail', '1.0', cran_options),
    ('maps', '3.2.0', cran_options),
    ('mapdata', '2.2-6', cran_options),
    ('mapproj', '1.2-5', cran_options),
    ('maptools', '0.9-2', cran_options),
    ('Matrix.utils', '0.9.6', cran_options),
    ('tensorA', '0.36', cran_options),
    ('MCMCglmm', '2.25', cran_options),
    ('mda', '0.4-10', cran_options),
    ('measurements', '1.2.0', cran_options),
    ('mediation', '4.4.6', cran_options),
    ('memisc', '0.99.14.9', cran_options),
    ('MetABEL', '0.2-0', cran_options),
    ('metap', '0.8', cran_options),
    ('mice', '2.46.0', cran_options),
    ('microbenchmark', '1.4-4', cran_options),
    ('mix', '1.0-10', cran_options),
    ('segmented', '0.5-3.0', cran_options),
    ('mixtools', '1.1.0', cran_options),
    ('mlbench', '2.1-1', cran_options),
    ('MLmetrics', '1.1.1', cran_options),
    ('mockery', '0.4.1', cran_options),
    ('mockr', '0.1', cran_options),
    ('modelr', '0.1.1', cran_options),
    ('mratios', '1.3.17', cran_options),
    ('msm', '1.6.6', cran_options),
    ('MSwM', '1.2', cran_options),
    ('multcompView', '0.1-7', cran_options),
    ('RcppCCTZ', '0.2.3', cran_options),
    ('nanotime', '0.2.0', cran_options),
    ('NISTunits', '1.0.1', cran_options),
    ('NMF', '0.21.0', cran_options),
    ('nortest', '1.0-4', cran_options),
    ('nws', '1.7.0.1', cran_options),
    ('nycflights13', '0.2.2', cran_options),
    ('openair', '2.3-0', cran_options),
    ('optparse', '1.4.4', cran_options),
    ('orcutt', '2.2', cran_options),
    ('ucminf', '1.1-4', cran_options),
    ('ordinal', '2015.6-28', cran_options),
    ('orientlib', '0.10.3', cran_options),
    ('osmar', '1.1-7', cran_options),
    ('outliers', '0.14', cran_options),
    ('oz', '1.0-21', cran_options),
    ('pamr', '1.55', cran_options),
    ('pander', '0.6.1', cran_options),
    ('strucchange', '1.5-1', cran_options),
    ('party', '1.2-4', cran_options),
    ('pbapply', '1.3-4', cran_options),
    ('PBSmapping', '2.70.4', cran_options),
    ('PBSmodelling', '2.68.6', cran_options),
    ('pcse', '1.9', cran_options),
    ('pder', '1.0-0', cran_options),
    ('pdfCluster', '1.0-2', cran_options),
    ('penalized', '0.9-50', cran_options),
    ('PerformanceAnalytics', '1.5.2', cran_options),
    ('pglm', '0.2-1', cran_options),
    ('pinp', '0.0.4', cran_options),
    ('pixmap', '0.4-11', cran_options),
    ('pkgKitten', '0.1.4', cran_options),
    ('plotly', '4.7.1', cran_options),
    ('poLCA', '1.4.1', cran_options),
    ('polyclip', '1.6-1', cran_options),
    ('polyester', '1.14.1', bioconductor_options),
    ('PredictABEL', '1.2-2', cran_options),
    ('pROC', '1.11.0', cran_options),
    ('processx', '2.0.0.1', cran_options),
    ('pryr', '0.1.4', cran_options),
    ('pscl', '1.5.2', cran_options),
    ('quantsmooth', '1.44.0', bioconductor_options),
    ('R.methodsS3', '1.7.1', cran_options),
    ('R.oo', '1.21.0', cran_options),
    ('R.utils', '2.6.0', cran_options),
    ('R.cache', '0.13.0', cran_options),
    ('R.rsp', '0.42.0', cran_options),
    ('R2Cuba', '1.1-0', cran_options),
    ('randomForest', '4.6-14', cran_options),
    ('ranger', '0.9.0', cran_options),
    ('RANN', '2.5.1', cran_options),
    ('rasterVis', '0.43', cran_options),
    ('readstata13', '0.9.0', cran_options),
    ('readxl', '1.0.0', cran_options),
    ('RcmdrMisc', '1.0-9', cran_options),
    ('tcltk2', '1.2-11', cran_options),
    ('Rcmdr', '2.4-2', cran_options),
    ('RcppProgress', '0.4', cran_options),
    ('rem', '1.2.8', cran_options),
    ('reprex', '0.1.2', cran_options),
    ('reticulate', '1.6', cran_options),
    ('RGraphics', '2.0-14', cran_options),
    ('rJava', '0.9-9', cran_options),
    ('rjson', '0.2.15', cran_options),
    ('rlecuyer', '0.3-4', cran_options),
    ('rmeta', '3.0', cran_options),
    ('Rmisc', '1.5', cran_options),
    ('rrcov', '1.4-3', cran_options),
    ('robust', '0.4-18', cran_options),
    ('roxygen2', '6.0.1', cran_options),
    ('rphast', '1.6.9', cran_options),
    ('RSclient', '0.7-3', cran_options),
    ('subprocess', '0.8.2', cran_options),
    ('wdman', '0.2.2', cran_options),
    ('RSelenium', '1.7.1', cran_options),
    ('Rserve', '1.7-3', cran_options),
    ('rsm', '2.9', cran_options),
    ('rstanarm', '2.17.3', cran_options),
    ('rticles', '0.4.1', cran_options),
    ('Rtsne', '0.13', cran_options),
    ('RUnit', '0.4.31', cran_options),
    ('rversions', '1.0.3', cran_options),
    ('selectr', '0.4-0', cran_options),
    ('rvest', '0.3.2', cran_options),
    ('satellite', '1.0.1', cran_options),
    ('SDMTools', '1.1-221', cran_options),
    ('sets', '1.0-18', cran_options),
    ('tsne', '0.1-3', cran_options),
    ('VGAM', '1.0-5', cran_options),
    ('sn', '1.5-1', cran_options),
    ('tclust', '1.3-1', cran_options),
    ('Seurat', '2.3.0', cran_options),
    ('sysfonts', '0.7.2', cran_options),
    ('showtextdb', '2.0', cran_options),
    ('showtext', '0.5-1', cran_options),
    ('SimComp', '3.2', cran_options),
    ('sm', '2.2-5.4', cran_options),
    ('soiltexture', '1.4.5', cran_options),
    ('spatstat.utils', '1.8-0', cran_options),
    ('spatstat.data', '1.2-0', cran_options),
    ('tensor', '1.5', cran_options),
    ('spatstat', '1.55-0', cran_options),
    ('spelling', '1.1', cran_options),
    ('splm', '1.4-10', cran_options),
    ('spls', '2.2-2', cran_options),
    ('stargazer', '5.2.1', cran_options),
    ('subselect', '0.14', cran_options),
    ('superpc', '1.09', cran_options),
    ('svglite', '1.2.1', cran_options),
    ('svGUI', '0.9-55', cran_options),
    ('svUnit', '0.7-12', cran_options),
    ('symbols', '1.1', cran_options),
    ('uuid', '0.1-2', cran_options),
    ('synchronicity', '1.3.2', cran_options),
    ('tables', '0.8.3', cran_options),
    ('testit', '0.7', cran_options),
    ('tidyverse', '1.2.1', cran_options),
    ('tikzDevice', '0.11', cran_options),
    ('tnam', '1.6.5', cran_options),
    ('tripack', '1.3-8', cran_options),
    ('tufte', '0.3', cran_options),
    ('tweenr', '0.1.5', cran_options),
    ('urca', '1.3-0', cran_options),
    ('vars', '1.5-2', cran_options),
    ('vcd', '1.4-4', cran_options),
    ('vcdExtra', '0.7-1', cran_options),
    ('vdiffr', '0.2.2', cran_options),
    ('venneuler', '1.1-0', cran_options),
    ('VGAMdata', '1.0-3', cran_options),
    ('vioplot', '0.2', cran_options),
    ('vrmlgen', '1.4.9', cran_options),
    ('webshot', '0.5.0', cran_options),
    ('webutils', '0.6', cran_options),
    ('WES.1KG.WUGSC', '1.10.0', bioconductor_options),
    ('xergm', '1.8.2', cran_options),
    ('xhmmScripts', '1.1', cran_options),
    ('xlsxjars', '0.6.1', cran_options),
    ('xlsx', '0.5.7', cran_options),
    ('zipcode', '1.0', cran_options),
    ('ztable', '0.1.5', cran_options),
