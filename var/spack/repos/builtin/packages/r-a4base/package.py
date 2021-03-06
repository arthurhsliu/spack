##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RA4base(RPackage):
    """Automated Affymetrix Array Analysis."""

    homepage = "https://www.bioconductor.org/packages/a4Base/"
    url      = "https://www.bioconductor.org/packages/release/bioc/src/contrib/a4Base_1.24.0.tar.gz"
    list_url = homepage
    version('1.24.0', '98f53cb437f1b8bb7ba8c2628c0f44c6')

    depends_on('r-biobase', type=('build', 'run'))
    depends_on('r-annotationdbi', type=('build', 'run'))
    depends_on('r-annaffy', type=('build', 'run'))
    depends_on('r-mpm', type=('build', 'run'))
    depends_on('r-genefilter', type=('build', 'run'))
    depends_on('r-limma', type=('build', 'run'))
    depends_on('r-multtest', type=('build', 'run'))
    depends_on('r-glmnet', type=('build', 'run'))
    depends_on('r-a4preproc', type=('build', 'run'))
    depends_on('r-a4core', type=('build', 'run'))
    depends_on('r-gplots', type=('build', 'run'))
