%define		php_name	php%{?php_suffix}
%define		modname	cvsclient
%define		status		beta
Summary:	%{modname} - CVS pserver client
Summary(pl.UTF-8):	%{modname} - klient CVS pserver
Name:		%{php_name}-pecl-%{modname}
Version:	0.2
Release:	6
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	d25ca6d7797118edf37817fcb7e93bc7
URL:		http://pecl.php.net/package/cvsclient/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pserver client extension. Current version has read-only streams
wrapper. Later versions to include commit/diff/log support.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Moduł klienta CVS pserver. Na chwilę obecną dostępne jest wsparcie
tylko 'read only'. W następnych wersjach planowane jest wsparcie dla
komend commit/diff/log.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
