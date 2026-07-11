%global tl_name ionumbers
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.3
Release:	%{tl_revision}.1
Summary:	Restyle numbers in maths mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ionumbers
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ionumbers.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ionumbers.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ionumbers.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
'ionumbers' stands for 'input/output numbers'. The package restyles
numbers in maths mode. If a number in the input file is written, e.g.,
as $3,231.44$ as commonly used in English texts, the package is able to
restyle it to be output as $3\,231{,}44$ as commonly used in German
texts (and vice versa). This may be useful, for example, if you have a
large table and want to include it in texts with different output
conventions without the need to change the table. The package can also
automatically group digits left of the decimal separator (thousands) and
right of the decimal separator (thousandths) in triplets without the
need of specifying commas (English) or points (German) as separators.
E.g., the input $1234.567890$ can be output as $1\,234.\,567\,890$.
Finally, an e starts the exponent of the number. For example, $21e6$ may
be output as $26\times10\,^{6}$.

