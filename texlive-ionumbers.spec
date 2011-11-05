# revision 23380
# category Package
# catalog-ctan /macros/latex/contrib/ionumbers
# catalog-date 2011-06-15 09:16:20 +0200
# catalog-license gpl
# catalog-version 0.3.1-alpha
Name:		texlive-ionumbers
Version:	0.3.1alpha
Release:	1
Summary:	Restyle numbers in maths mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ionumbers
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ionumbers.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ionumbers.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ionumbers.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
'ionumbers' stands for 'input/output numbers'. The package
restyles numbers in maths mode. If a number in the input file
is written, e.g., as $3,231.44$ as commonly used in English
texts, the package is able to restyle it to be output as
$3\,231{,}44$ as commonly used in German texts (and vice
versa). This may be useful, for example, if you have a large
table and want to include it in texts with different output
conventions without the need to change the table. The package
can also automatically group digits left of the decimal
separator (thousands) and right of the decimal separator
(thousandths) in triplets without the need of specifing commas
(English) or points (German) as separators. E.g., the input
$1234.567890$ can be output as $1\,234.\,567\,890$. Finally, an
e starts the exponent of the number. For example, $21e6$ may be
output as $26\times10\,^{6}$.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ionumbers/ionumbers.sty
%doc %{_texmfdistdir}/doc/latex/ionumbers/COPYING
%doc %{_texmfdistdir}/doc/latex/ionumbers/Makefile
%doc %{_texmfdistdir}/doc/latex/ionumbers/README
%doc %{_texmfdistdir}/doc/latex/ionumbers/ionumbers.pdf
%doc %{_texmfdistdir}/doc/latex/ionumbers/ionumbers_test.pdf
%doc %{_texmfdistdir}/doc/latex/ionumbers/ionumbers_test.tex
#- source
%doc %{_texmfdistdir}/source/latex/ionumbers/ionumbers.dtx
%doc %{_texmfdistdir}/source/latex/ionumbers/ionumbers.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
