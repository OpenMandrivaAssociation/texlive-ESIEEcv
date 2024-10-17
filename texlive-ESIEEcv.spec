Name:		texlive-ESIEEcv
Version:	59638
Release:	2
Summary:	Curriculum vitae for French use
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ESIEEcv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esieecv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esieecv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esieecv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to set up a curriculum vitae as a
French employer will expect.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/esieecv
%doc %{_texmfdistdir}/doc/latex/esieecv
#- source
%doc %{_texmfdistdir}/source/latex/esieecv

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
