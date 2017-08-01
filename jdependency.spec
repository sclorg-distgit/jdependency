%{?scl:%scl_package jdependency}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}jdependency
Version:        1.1
Release:        2.1%{?dist}
Summary:        This project provides an API to analyse class dependencies
License:        ASL 2.0
URL:            http://github.com/tcurdt/%{pkg_name}
BuildArch:      noarch

Source0:        http://github.com/tcurdt/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(commons-io:commons-io)
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.ow2.asm:asm)
BuildRequires:  %{?scl_prefix}mvn(org.ow2.asm:asm-analysis)
BuildRequires:  %{?scl_prefix}mvn(org.ow2.asm:asm-commons)
BuildRequires:  %{?scl_prefix}mvn(org.ow2.asm:asm-tree)
BuildRequires:  %{?scl_prefix}mvn(org.ow2.asm:asm-util)

%description
%{pkg_name} is small library that helps you analyze class level
dependencies, clashes and missing classes.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
%mvn_file : %{pkg_name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.1-2.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 06 2016 Michael Simacek <msimacek@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Michal Srb <msrb@redhat.com> - 0.9-1
- Update to upstream version 0.9

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7-10
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-8
- Update to current packaging guidelines
- Fix test failures

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-7
- Remove unneeded BR: maven-idea-plugin

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.7-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7-3
- Fix date ordering in changelog
- Guidelines fixes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7-1
- Update to 0.7
- Fix BR to not require maven2
- Fix BR for new package name
- Adjust spec to new guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-3
- Add license to javadoc subpackage
- Change jakarta-commons-io for apache-commons-io
- Add BR to maven

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-2
- Rename from vafer-jdependency to jdependency alone

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-1
- Initial package
