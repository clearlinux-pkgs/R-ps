#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ps
Version  : 1.6.0
Release  : 33
URL      : https://cran.r-project.org/src/contrib/ps_1.6.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ps_1.6.0.tar.gz
Summary  : List, Query, Manipulate System Processes
Group    : Development/Tools
License  : MIT
Requires: R-ps-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
'Linux' and 'macOS'.

%package lib
Summary: lib components for the R-ps package.
Group: Libraries

%description lib
lib components for the R-ps package.


%prep
%setup -q -c -n ps
cd %{_builddir}/ps

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614624868

%install
export SOURCE_DATE_EPOCH=1614624868
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ps
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ps
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ps
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ps || :


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
