#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: 537da87
#
Name     : R-ps
Version  : 1.7.6
Release  : 56
URL      : https://cran.r-project.org/src/contrib/ps_1.7.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ps_1.7.6.tar.gz
Summary  : List, Query, Manipulate System Processes
Group    : Development/Tools
License  : MIT
Requires: R-ps-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
'Windows', 'Linux' and 'macOS'.

%package lib
Summary: lib components for the R-ps package.
Group: Libraries

%description lib
lib components for the R-ps package.


%prep
%setup -q -n ps
pushd ..
cp -a ps buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1705587649

%install
export SOURCE_DATE_EPOCH=1705587649
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ps/DESCRIPTION
/usr/lib64/R/library/ps/INDEX
/usr/lib64/R/library/ps/LICENSE
/usr/lib64/R/library/ps/Meta/Rd.rds
/usr/lib64/R/library/ps/Meta/features.rds
/usr/lib64/R/library/ps/Meta/hsearch.rds
/usr/lib64/R/library/ps/Meta/links.rds
/usr/lib64/R/library/ps/Meta/nsInfo.rds
/usr/lib64/R/library/ps/Meta/package.rds
/usr/lib64/R/library/ps/NAMESPACE
/usr/lib64/R/library/ps/NEWS.md
/usr/lib64/R/library/ps/R/ps
/usr/lib64/R/library/ps/R/ps.rdb
/usr/lib64/R/library/ps/R/ps.rdx
/usr/lib64/R/library/ps/WORDLIST
/usr/lib64/R/library/ps/bin/px
/usr/lib64/R/library/ps/help/AnIndex
/usr/lib64/R/library/ps/help/aliases.rds
/usr/lib64/R/library/ps/help/paths.rds
/usr/lib64/R/library/ps/help/ps.rdb
/usr/lib64/R/library/ps/help/ps.rdx
/usr/lib64/R/library/ps/html/00Index.html
/usr/lib64/R/library/ps/html/R.css
/usr/lib64/R/library/ps/internals.md
/usr/lib64/R/library/ps/tests/testthat.R
/usr/lib64/R/library/ps/tests/testthat/helpers.R
/usr/lib64/R/library/ps/tests/testthat/test-cleanup-reporter.R
/usr/lib64/R/library/ps/tests/testthat/test-common.R
/usr/lib64/R/library/ps/tests/testthat/test-connections.R
/usr/lib64/R/library/ps/tests/testthat/test-finished.R
/usr/lib64/R/library/ps/tests/testthat/test-kill-tree.R
/usr/lib64/R/library/ps/tests/testthat/test-linux.R
/usr/lib64/R/library/ps/tests/testthat/test-macos.R
/usr/lib64/R/library/ps/tests/testthat/test-pid-reuse.R
/usr/lib64/R/library/ps/tests/testthat/test-posix-zombie.R
/usr/lib64/R/library/ps/tests/testthat/test-posix.R
/usr/lib64/R/library/ps/tests/testthat/test-ps.R
/usr/lib64/R/library/ps/tests/testthat/test-system.R
/usr/lib64/R/library/ps/tests/testthat/test-utils.R
/usr/lib64/R/library/ps/tests/testthat/test-windows.R
/usr/lib64/R/library/ps/tests/testthat/test-winver.R
/usr/lib64/R/library/ps/tools/error-codes.R
/usr/lib64/R/library/ps/tools/winver.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ps/libs/ps.so
/usr/lib64/R/library/ps/libs/ps.so.avx2
/usr/lib64/R/library/ps/libs/ps.so.avx512
