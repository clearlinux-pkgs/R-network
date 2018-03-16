#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-network
Version  : 1.13.0
Release  : 1
URL      : https://cran.r-project.org/src/contrib/network_1.13.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/network_1.13.0.tar.gz
Summary  : Classes for Relational Data
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-network-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-network package.
Group: Libraries

%description lib
lib components for the R-network package.


%prep
%setup -q -c -n network

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521231292

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521231292
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library network
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library network
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library network
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library network|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/network/CITATION
/usr/lib64/R/library/network/DESCRIPTION
/usr/lib64/R/library/network/INDEX
/usr/lib64/R/library/network/Meta/Rd.rds
/usr/lib64/R/library/network/Meta/data.rds
/usr/lib64/R/library/network/Meta/features.rds
/usr/lib64/R/library/network/Meta/hsearch.rds
/usr/lib64/R/library/network/Meta/links.rds
/usr/lib64/R/library/network/Meta/nsInfo.rds
/usr/lib64/R/library/network/Meta/package.rds
/usr/lib64/R/library/network/Meta/vignette.rds
/usr/lib64/R/library/network/NAMESPACE
/usr/lib64/R/library/network/R/network
/usr/lib64/R/library/network/R/network.rdb
/usr/lib64/R/library/network/R/network.rdx
/usr/lib64/R/library/network/data/emon.RData
/usr/lib64/R/library/network/data/flo.RData
/usr/lib64/R/library/network/doc/index.html
/usr/lib64/R/library/network/doc/networkVignette.R
/usr/lib64/R/library/network/doc/networkVignette.Rnw
/usr/lib64/R/library/network/doc/networkVignette.pdf
/usr/lib64/R/library/network/help/AnIndex
/usr/lib64/R/library/network/help/aliases.rds
/usr/lib64/R/library/network/help/network.rdb
/usr/lib64/R/library/network/help/network.rdx
/usr/lib64/R/library/network/help/paths.rds
/usr/lib64/R/library/network/html/00Index.html
/usr/lib64/R/library/network/html/R.css
/usr/lib64/R/library/network/include/netregistration.h
/usr/lib64/R/library/network/include/network.h
/usr/lib64/R/library/network/libs/symbols.rds
/usr/lib64/R/library/network/network.api/networkapi.c
/usr/lib64/R/library/network/network.api/networkapi.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/network/libs/network.so
/usr/lib64/R/library/network/libs/network.so.avx2
/usr/lib64/R/library/network/libs/network.so.avx512
